# Facebook Feed Ranking 系统设计总结

> 基于 Meta MLE 模拟面试整理，2026-04-16

---

## 一、需求澄清

### 功能需求
- 从海量候选内容中，为每个用户选出最相关的内容展示
- 支持一对一好友动态、关注主页、推荐内容

### 非功能需求
| 指标 | 要求 |
|------|------|
| 候选集规模 | 50万 ~ 100万 条/用户 |
| 最终曝光数 | 20 ~ 50 条/次刷新 |
| DAU | 20亿 |
| QPS | ~200,000（峰值 ×3 ≈ 600K） |
| 延迟 | p99 < 200ms（端到端） |
| 关键目标 | 最大化用户**长期留存** |
| 约束目标 | 内容安全、广告占比、用户体验 |

---

## 二、整体架构

```
100万候选池
     ↓
【召回层 Recall】      100万 → 几千    延迟 < 50ms
     ↓
【粗排层 Prerank】     几千  → 几百    延迟 < 30ms
     ↓
【精排层 Rank】        几百  → 几十    延迟 < 100ms
     ↓
【重排层 Mix】         几十  → 最终展示  延迟 < 20ms
     ↓
最终 Feed（20~50条）   端到端 < 200ms
```

---

## 三、召回层（Recall）

### 目标
从 100万 候选中快速筛选出 几千 条相关内容。

### 多路召回策略

#### U2U（User to User）—— 找相似用户
- **协同过滤**：基于行为矩阵计算用户相似度
- **User Embedding**：训练用户向量，用 ANN 检索相似用户
- 适合：破圈推荐，发现社交关系弱但兴趣相近的用户内容

#### I2I（Item to Item）—— 找相似内容
- **ItemCF**：基于共现关系计算物品相似度
- **Item Embedding**：行为序列当句子，item 当词，训练 Embedding
- **Graph Embedding**：PinSage/GraphSAGE，利用社交图结构
- 适合：用户最近交互内容的"续集"，精准度高

#### U2I（User to Item）—— 用户直接匹配内容（主力）
- **双塔模型（Two-Tower）**：User Tower + Item Tower，最后内积
- **序列模型**：SASRec / BERT4Rec，建模用户历史行为序列
- 适合：个性化程度最高，是召回层核心

### 向量检索加速（ANN）

#### IVFPQ（工业界主流）
```
Step 1 - IVF（Inverted File Index）：
  对全量 Item Embedding 做 K-Means 聚类
  → 检索时只在最近的 Top-K 簇内搜索
  → 从百万 → 几千候选

Step 2 - PQ（Product Quantization）：
  将高维向量切成 M 段，每段独立量化
  每段用 K=256 个聚类中心（1 byte）表示
  → 压缩比 64x（512bytes → 8bytes）
  → 用查找表代替实际向量计算，极快
```

**PQ 的误差来源**：用聚类中心代替真实子向量（量化误差）

**OPQ 优化**：先做正交旋转使各维度独立，再做 PQ，减少量化误差

#### HNSW
- 多层图结构，召回率比 IVF 更高
- 缺点：内存占用大

#### 对比
| 方法 | 速度 | 召回率 | 内存 |
|------|------|--------|------|
| 暴力搜索 | ❌ | 100% | ✅ |
| IVFPQ | ✅ | 95%+ | ✅ |
| HNSW | ✅ | 98%+ | ❌ |

### 多路召回融合
- 各路分配动态比例，根据后续每路实际曝光占比反馈调整
- 简单合并后送入 Prerank 统一打分

---

## 四、粗排层（Prerank）

### 目标
从几千条中筛选出几百条，在更短时间内完成大规模打分。

### 设计选择：增强版双塔模型
- 继承召回层的双塔架构（保证速度）
- 使用**更丰富的特征**（比召回层更多的商家特征、User×Item 交叉特征）
- Item Embedding 可预计算，在线只需计算 User Embedding + 内积

### 双塔的根本缺陷
> User 和 Item 的特征只在最后内积时"见面"，表达能力有限，无法做深度特征交叉。
> 这正是精排存在的必要性。

---

## 五、精排层（Rank）

### 目标
从几百条中精细打分，选出最终几十条。支持深度 User × Item 特征交叉。

### 模型结构：DIN（Deep Interest Network）+ 多目标 MLP

```
输入特征：
  ├── 用户画像特征（年龄、性别、历史购买/曝光概率）
  │       ↓ Embedding → 1维向量
  ├── 用户序列特征（过去行为序列）
  │       ↓ Embedding → 2维序列
  │       ↓ Target Attention（以当前 Item 为 Query）
  │       → 1维抽象用户兴趣向量
  └── 商家/内容特征（ID、类别、User×Item 历史交互）
          ↓ Embedding → 1维向量
          
三类特征拼接 → MLP（多层特征交叉）→ 多个输出头
```

### Target Attention（DIN 核心）
```
用户序列（历史点击）作为 Key/Value
当前候选 Item 作为 Query
→ Attention 权重 = softmax(Query · Key^T)
→ 加权求和得到与当前 Item 相关的用户兴趣表达
→ 避免所有历史行为等权重混合，更精准
```

### 多目标训练
```
多个独立的输出头 + 各自的 Loss：
  Head 1: P(like)     → Binary Cross Entropy
  Head 2: P(comment)  → Binary Cross Entropy
  Head 3: P(share)    → Binary Cross Entropy
  Head 4: P(hide)     → Binary Cross Entropy

总 Loss = Σ λᵢ × Lossᵢ
```

---

## 六、重排层（Mix）

### 目标
融合多目标分数，叠加业务规则，输出最终排序。

### 1. 多目标分数融合
```
final_score = w1×f(P_like) + w2×f(P_comment) + w3×f(P_share)
            - w4×f(P_hide) + w5×生态分

f() = 校准函数（Calibration），统一各目标量纲
权重 w 通过 A/B 测试与长期留存相关性标定
```

### 2. 多样性保证（Diversity）
- **MMR（Maximal Marginal Relevance）**：
  ```
  score_i = λ × relevance_i - (1-λ) × max_sim(i, already_selected)
  ```
- **硬规则**：同一作者最多出现 N 条、同一话题最多 M 条、内容类型交替

### 3. 内容安全过滤（Hard Filter）
- 过滤有害内容、已屏蔽作者、已看过内容、违规内容
- Mix 层是最终兜底防线

### 4. 广告插入
- 有机内容排序后，按策略在特定位置插入广告
- 广告有独立排序系统（CTR × bid_price）
- 控制广告密度（如每5条有机内容插1条广告）

### 5. 生态干预（Business Rules）
- 新内容/新创作者扶持（冷启动）
- 特殊事件优先级提升
- 用户手动置顶的好友/主页

---

## 七、长期留存优化

### 核心问题
短期代理指标（点赞、评论）≠ 长期留存目标

**经典反例**：标题党 → 短期 CTR ↑ → 用户满意度 ↓ → 长期留存 ↓

### 解决方案

#### 1. 优化代理指标组合
```
正向信号：完播率、收藏、回访、主动搜索
负向信号：划走、举报、看完即关闭 App
→ 比单纯的"点赞/评论"更能反映真实满意度
```

#### 2. 留存预测辅助任务
- 将"用户次日/次周是否活跃"作为辅助 Label
- 与短期目标联合训练（Multi-task Learning）

#### 3. 强化学习（前沿方向）
```
把 Feed 推荐看成序列决策：
  State:  用户当前状态
  Action: 推荐哪条内容
  Reward: 即时反馈
  目标:   最大化长期累计 Reward（留存）

算法：DQN / Actor-Critic / Offline RL
Meta 实际用于 Reels 推荐优化
```

#### 4. 多样性与探索（Exploration）
```
ε-greedy：有 ε% 概率随机探索非最优内容
UCB：score = exploit_score + α × exploration_bonus
          exploration_bonus 与曝光次数负相关
→ 避免信息茧房，长期提升留存
```

#### 5. A/B 测试 + 长期指标追踪
- 短期指标（CTR、时长）和长期指标（7日/30日留存）同时监控
- 短期好的模型，持续追踪长期影响，必要时回滚

---

## 八、常见追问与答案

| 追问 | 答案要点 |
|------|---------|
| 为什么粗排用双塔而不是 MLP？ | 双塔的 Item Embedding 可预计算，延迟低；MLP 必须实时计算每个 pair |
| 精排和粗排的本质区别？ | 精排支持 User×Item 深度特征交叉；双塔只有最后内积这一次交叉 |
| Position Bias 怎么处理？ | 训练时加入曝光位置作为特征，或用 PAL（Position-Aware Learning）消偏 |
| 模型多久重训一次？ | 精排每天全量重训；结合近线增量学习（Kafka 流式消费新数据） |
| 冷启动怎么处理？ | 新用户用人口统计学特征 + 兴趣选择；新内容基于语义特征 + 小流量试投 |
| 特征穿越（Data Leakage）？ | 不能用"最终点赞数"，只能用"发布后1小时内点赞数"等预测时可获得的特征 |

---

## 九、参考资料

| 资源 | 说明 |
|------|------|
| [Designing ML Systems - Chip Huyen](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) | MLE 必读书 |
| [Meta DLRM 论文](https://arxiv.org/abs/1906.00091) | Meta 推荐系统架构 |
| [DIN 论文（阿里）](https://arxiv.org/abs/1706.06978) | Target Attention 的来源 |
| [Meta Faiss](https://github.com/facebookresearch/faiss) | ANN 向量检索库 |
| [Designing Data-Intensive Applications](https://dataintensive.net/) | 系统设计基础 |

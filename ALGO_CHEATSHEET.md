# 🚀 算法面试速查手册（2026）

> 根据已做题目整理，按题型分类，包含核心思路、代码模板和复杂度分析。

---

## 目录

1. [哈希表 (Hash Table)](#1-哈希表)
2. [双指针 (Two Pointers)](#2-双指针)
3. [滑动窗口 (Sliding Window)](#3-滑动窗口)
4. [链表 (Linked List)](#4-链表)
5. [栈 (Stack)](#5-栈)
6. [动态规划 - 一维 (DP 1D)](#6-动态规划---一维)
7. [动态规划 - 网格/路径 (DP Grid)](#7-动态规划---网格路径)
8. [动态规划 - 字符串 (DP String)](#8-动态规划---字符串)
9. [动态规划 - 区间 (DP Interval)](#9-动态规划---区间)
10. [堆 / 优先队列 (Heap)](#10-堆--优先队列)
11. [图 - DFS/BFS (Graph)](#11-图---dfsbfs)
12. [图 - 拓扑排序 (Topological Sort)](#12-图---拓扑排序)
13. [前缀积/前缀和 (Prefix)](#13-前缀积前缀和)
14. [排列与下一个排列 (Permutation)](#14-排列与下一个排列)
15. [位运算 / 快速幂 (Bit / Fast Power)](#15-位运算--快速幂)
16. [数学 / 几何 (Math)](#16-数学--几何)
17. [区间排序 (Interval)](#17-区间排序)
18. [字典树 Trie](#18-字典树-trie)

---

## 1. 哈希表

### 核心思路
- 用 `dict` 或 `set` 实现 O(1) 查找
- **经典模式**：遍历时查 `target - num` 是否存在

### 代表题目

| 题号 | 题目 | 难度 |
|------|------|------|
| 1 | Two Sum | Easy |

### 代码模板

```python
# Two Sum - O(n) 时间，O(n) 空间
def twoSum(nums, target):
    seen = {}                         # {value: index}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```

---

## 2. 双指针

### 核心思路
- **对撞指针**：从两端向中间，用于有序数组/找最优对
- **同向指针**：快慢指针，用于链表中点/环/删元素
- 移动原则：每次移动「更无价值」的那端

### 代表题目

| 题号 | 题目 | 难度 | 关键点 |
|------|------|------|--------|
| 11 | Container With Most Water | Medium | 移动较矮边 |
| 680 | Valid Palindrome II | Easy | 遇不匹配时分别尝试跳过左/右 |
| 15 | 3Sum | Medium | 排序后双指针 |

### 代码模板

```python
# 对撞双指针 - Container With Most Water
def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1        # 移动较矮的那端
        else:
            right -= 1
    return max_area

# 回文验证（可删一个字符）- Valid Palindrome II
def validPalindrome(s):
    def isPalin(s, l, r):
        while l < r:
            if s[l] != s[r]: return False
            l += 1; r -= 1
        return True
    
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return isPalin(s, l+1, r) or isPalin(s, l, r-1)
        l += 1; r -= 1
    return True
```

---

## 3. 滑动窗口

### 核心思路
- 维护一个满足条件的窗口 `[left, right)`
- 扩展 `right`；当窗口不满足条件时，收缩 `left`
- 用 `dict/set` 记录窗口内的状态

### 代表题目

| 题号 | 题目 | 难度 | 窗口条件 |
|------|------|------|----------|
| 3 | Longest Substring Without Repeating Characters | Medium | 无重复字符 |
| 1004 | Max Consecutive Ones III | Medium | 0 的个数 ≤ k |
| 76 | Minimum Window Substring | Hard | 包含所有目标字符 |
| 424 | Longest Repeating Character Replacement | Medium | 替换次数 ≤ k |

### 代码模板

```python
# 滑动窗口通用模板
def slidingWindow(s, k):
    left = 0
    counter = {}  # 窗口内的状态
    result = 0
    
    for right in range(len(s)):
        # 1. 将 s[right] 加入窗口
        counter[s[right]] = counter.get(s[right], 0) + 1
        
        # 2. 当窗口不满足条件时，收缩左边
        while not valid(counter):  # 根据题意判断
            counter[s[left]] -= 1
            if counter[s[left]] == 0:
                del counter[s[left]]
            left += 1
        
        # 3. 更新结果
        result = max(result, right - left + 1)
    
    return result

# 1004: Max Consecutive Ones III（计数 0 的个数）
def longestOnes(nums, k):
    left = n_zeros = 0
    result = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            n_zeros += 1
        if n_zeros > k:            # 窗口超限，收缩
            if nums[left] == 0:
                n_zeros -= 1
            left += 1
        result = max(result, right - left + 1)
    return result
```

---

## 4. 链表

### 核心思路
- **虚拟头节点（Dummy Head）**：简化头节点特殊处理
- **反转链表**：prev/curr 两个指针迭代
- **分治归并**：K 路归并链表，两两合并

### 代表题目

| 题号 | 题目 | 难度 | 方法 |
|------|------|------|------|
| 23 | Merge K Sorted Lists | Hard | 最小堆 or 分治归并 |
| 25 | Reverse Nodes in k-Group | Hard | 模拟 + 反转子链表 |

### 代码模板

```python
# 反转链表（基础操作）
def reverseList(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# K 路归并 - 分治法 (LeetCode 23)
def mergeKLists(lists):
    if not lists: return None
    if len(lists) == 1: return lists[0]
    mid = len(lists) // 2
    left = mergeKLists(lists[:mid])
    right = mergeKLists(lists[mid:])
    return mergeTwoLists(left, right)

def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
    cur = dummy
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1; l1 = l1.next
        else:
            cur.next = l2; l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

# K 路归并 - 最小堆法 (LeetCode 23)
import heapq
def mergeKLists_heap(lists):
    dummy = ListNode(0)
    cur = dummy
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    while heap:
        val, i, node = heapq.heappop(heap)
        cur.next = node
        cur = cur.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next

# Reverse Nodes in k-Group (LeetCode 25)
def reverseKGroup(head, k):
    dummy = ListNode(0)
    dummy.next = head
    group_prev = dummy
    
    while True:
        # 找第 k 个节点（不足 k 个则退出）
        kth = get_kth(group_prev, k)
        if not kth: break
        
        group_next = kth.next
        
        # 反转 [group_prev.next, kth] 这 k 个节点
        prev, curr = kth.next, group_prev.next
        while curr != group_next:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # 接回链表
        tmp = group_prev.next
        group_prev.next = kth
        tmp.next = group_next
        group_prev = tmp
    
    return dummy.next

def get_kth(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr
```

---

## 5. 栈

### 核心思路
- **括号匹配**：遇 `(` 入栈，遇 `)` 弹栈；结束后栈中剩余的都是不匹配的
- **单调栈**：维护一个递增/递减的栈，用于「下一个更大/小元素」

### 代表题目

| 题号 | 题目 | 难度 | 方法 |
|------|------|------|------|
| 1249 | Minimum Remove to Make Valid Parentheses | Medium | 栈记录无效括号位置 |
| 84 | Largest Rectangle in Histogram | Hard | 单调栈 |

### 代码模板

```python
# 括号修复 - 最少删除使括号合法 (LeetCode 1249)
def minRemoveToMakeValid(s):
    stack = []          # 存 '(' 的下标
    remove = set()
    
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if stack:
                stack.pop()     # 匹配成功
            else:
                remove.add(i)   # 多余的 ')'
    
    remove |= set(stack)        # 未匹配的 '('
    return ''.join(c for i, c in enumerate(s) if i not in remove)
```

---

## 6. 动态规划 - 一维

### 代表题目

| 题号 | 题目 | 难度 | DP 含义 |
|------|------|------|---------|
| 264 | Ugly Number II | Medium | dp[i] = min(dp[p2]*2, dp[p3]*3, dp[p5]*5) |
| 300 | Longest Increasing Subsequence | Medium | dp[i] = 以 nums[i] 结尾的 LIS 长度 |
| 322 | Coin Change | Medium | dp[i] = 凑成金额 i 的最少硬币数 |

### 代码模板

```python
# Ugly Number II (LeetCode 264) - 三指针 DP
def nthUglyNumber(n):
    dp = [1] * n
    p2 = p3 = p5 = 0
    for i in range(1, n):
        nxt = min(dp[p2]*2, dp[p3]*3, dp[p5]*5)
        dp[i] = nxt
        if nxt == dp[p2]*2: p2 += 1
        if nxt == dp[p3]*3: p3 += 1
        if nxt == dp[p5]*5: p5 += 1
    return dp[n-1]

# Coin Change (LeetCode 322) - 背包 DP
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
```

---

## 7. 动态规划 - 网格/路径

### 核心思路
- `dp[i][j]` 通常从 `dp[i-1][j]` 和 `dp[i][j-1]` 转移
- **正向**（最短/最多路径）：从 `[0][0]` 到 `[m-1][n-1]`
- **逆向**（最小初始值）：从 `[m-1][n-1]` 反推，如地牢题

### 代表题目

| 题号 | 题目 | 难度 | DP 方向 |
|------|------|------|---------|
| 62 | Unique Paths | Medium | 正向，计数 |
| 64 | Minimum Path Sum | Medium | 正向，最小值 |
| 174 | Dungeon Game | Hard | **逆向**，最小初始血量 |

### 代码模板

```python
# Unique Paths (LeetCode 62)
def uniquePaths(m, n):
    dp = [[1]*n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]

# Minimum Path Sum (LeetCode 64)
def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j-1] + grid[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[m-1][n-1]

# Dungeon Game (LeetCode 174) - 逆向 DP
def calculateMinimumHP(dungeon):
    m, n = len(dungeon), len(dungeon[0])
    dp = [[0]*n for _ in range(m)]
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i == m-1 and j == n-1:
                dp[i][j] = max(1, 1 - dungeon[i][j])
            elif i == m-1:
                dp[i][j] = max(1, dp[i][j+1] - dungeon[i][j])
            elif j == n-1:
                dp[i][j] = max(1, dp[i+1][j] - dungeon[i][j])
            else:
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
    return dp[0][0]
```

---

## 8. 动态规划 - 字符串

### 核心思路
- `dp[i][j]` 表示 `s1[:i]` 和 `s2[:j]` 的某种关系
- 初始化：`dp[0][j]` 和 `dp[i][0]` 是边界（空串情况）
- 转移：字符相等 vs 不等 → 不同来源

### 代表题目对比

| 题号 | 题目 | 难度 | 转移（相等时） | 转移（不等时） |
|------|------|------|----------------|----------------|
| 1143 | LCS 最长公共子序列 | Medium | `dp[i-1][j-1] + 1` | `max(dp[i-1][j], dp[i][j-1])` |
| 72 | Edit Distance 编辑距离 | Medium | `dp[i-1][j-1]` | `1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])` |
| 115 | Distinct Subsequences 子序列个数 | Hard | `dp[i-1][j-1] + dp[i-1][j]` | `dp[i-1][j]` |
| 97 | Interleaving String | Medium | `dp[i-1][j]` or `dp[i][j-1]` | 条件 AND |
| 10 | Regular Expression Matching | Hard | 看是否 `.` 或精确匹配 | `*` 特殊处理 |
| 44 | Wildcard Matching | Medium | `dp[i-1][j-1]` | `*` → `dp[i-1][j] or dp[i][j-1]` |

### 代码模板

```python
# LCS (LeetCode 1143) - 最长公共子序列
def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

# Edit Distance (LeetCode 72) - 编辑距离
def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0] = i  # 删除 i 个字符
    for j in range(n+1): dp[0][j] = j  # 插入 j 个字符
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # 字符匹配，无需操作
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j-1],  # 替换
                    dp[i-1][j],    # 删除 word1[i-1]
                    dp[i][j-1]     # 插入 word2[j-1]
                )
    return dp[m][n]

# Distinct Subsequences (LeetCode 115)
def numDistinct(s, t):
    m, n = len(s), len(t)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0] = 1  # t 为空，方案数为 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j]  # 不选 s[i-1]
            if s[i-1] == t[j-1]:
                dp[i][j] += dp[i-1][j-1]  # 选 s[i-1]
    return dp[m][n]

# Interleaving String (LeetCode 97)
def isInterleave(s1, s2, s3):
    n1, n2, n3 = len(s1), len(s2), len(s3)
    if n1 + n2 != n3: return False
    dp = [[False]*(n2+1) for _ in range(n1+1)]
    dp[0][0] = True
    for i in range(1, n1+1):
        dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
    for j in range(1, n2+1):
        dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                       (dp[i][j-1] and s2[j-1] == s3[i+j-1])
    return dp[n1][n2]

# Wildcard Matching (LeetCode 44)
def isMatch_wildcard(s, p):
    m, n = len(s), len(p)
    dp = [[False]*(m+1) for _ in range(n+1)]
    dp[0][0] = True
    for i in range(1, n+1):         # p 以 '*' 开头可以匹配空串
        if p[i-1] == '*': dp[i][0] = dp[i-1][0]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if p[i-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]  # 空匹配 or 消耗一个s字符
            else:
                dp[i][j] = dp[i-1][j-1] and (p[i-1] == '?' or p[i-1] == s[j-1])
    return dp[n][m]

# Regular Expression Matching (LeetCode 10)
def isMatch_regex(s, p):
    m, n = len(s), len(p)
    dp = [[False]*(m+1) for _ in range(n+1)]
    dp[0][0] = True
    for i in range(2, n+1):         # "a*b*" 可以匹配空串
        if p[i-1] == '*': dp[i][0] = dp[i-2][0]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if p[i-1] == '.':
                dp[i][j] = dp[i-1][j-1]
            elif p[i-1] == '*':
                dp[i][j] = dp[i-2][j] or \    # '*' 匹配 0 次
                           (dp[i][j-1] and (p[i-2] == s[j-1] or p[i-2] == '.'))  # '*' 匹配 1+次
            else:
                dp[i][j] = dp[i-1][j-1] and p[i-1] == s[j-1]
    return dp[n][m]
```

---

## 9. 动态规划 - 区间

### 核心思路
- `dp[i][j]` 表示区间 `[i, j]` 的答案
- **枚举顺序**：外层枚举区间长度 `length`，内层枚举左端点 `i`
- 先算小区间，再扩展到大区间

### 代表题目

| 题号 | 题目 | 难度 | DP 含义 |
|------|------|------|---------|
| 516 | Longest Palindromic Subsequence | Medium | `dp[i][j]` = s[i..j] 最长回文子序列 |
| 1216 | Valid Palindrome III | Hard | 等价于 `len(s) - LPS(s) ≤ k` |

### 代码模板

```python
# Longest Palindromic Subsequence (LeetCode 516)
def longestPalindromeSubseq(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for i in range(n): dp[i][i] = 1   # 单字符，长度为 1
    
    for length in range(2, n+1):       # 枚举区间长度
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    return dp[0][n-1]

# Valid Palindrome III (LeetCode 1216) - 利用 LPS
def isValidPalindrome(s, k):
    # 最少删除数 = len(s) - LPS(s)
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for i in range(n): dp[i][i] = 1
    for length in range(2, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = (dp[i+1][j-1] if length > 2 else 0) + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return n - dp[0][n-1] <= k
```

---

## 10. 堆 / 优先队列

### 核心思路
- **K 路归并**（Min-Heap）：堆中维护各路当前最小值
- 堆元素格式：`(value, row, col)` 或 `(value, idx, node)`
- 每次弹出最小值后，将该路的下一个元素压入堆

### 代表题目

| 题号 | 题目 | 难度 | 场景 |
|------|------|------|------|
| 23 | Merge K Sorted Lists | Hard | K 路有序链表归并 |
| 373 | Find K Pairs with Smallest Sums | Medium | K 路有序序列归并 |
| 378 | Kth Smallest Element in Sorted Matrix | Medium | K 路矩阵归并 |

### 代码模板

```python
import heapq

# K 路归并通用模板
# 适用于：多路有序序列，合并/取前 K 小
def k_way_merge(matrix):
    """
    NxN 矩阵每行有序，返回所有元素排序后结果
    面试原题：给 N 个有序数组，合并
    """
    n = len(matrix)
    # 初始化：每行第一个元素入堆
    heap = [(matrix[i][0], i, 0) for i in range(n)]
    heapq.heapify(heap)
    
    result = []
    while heap:
        val, row, col = heapq.heappop(heap)
        result.append(val)
        if col + 1 < len(matrix[row]):
            heapq.heappush(heap, (matrix[row][col+1], row, col+1))
    
    return result

# Find K Pairs (LeetCode 373)
def kSmallestPairs(nums1, nums2, k):
    heap = []
    for i in range(min(len(nums1), k)):
        heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
    
    result = []
    while heap and len(result) < k:
        s, i, j = heapq.heappop(heap)
        result.append([nums1[i], nums2[j]])
        if j + 1 < len(nums2):
            heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
    return result
```

---

## 11. 图 - DFS/BFS

### 核心思路
- **DFS**：递归或显式栈，用于连通性/路径搜索
- **BFS**：队列，用于最短路径
- **关键桥（Bridge）**：Tarjan 算法，DFS 中用 disc 和 low 值判断

### 代表题目

| 题号 | 题目 | 难度 | 方法 |
|------|------|------|------|
| 200 | Number of Islands | Medium | DFS/BFS 淹没法 |
| 207/210 | Course Schedule I/II | Medium | DFS 环检测 |
| 1192 | Critical Connections (Bridge) | Hard | Tarjan 算法 |
| 269 | Alien Dictionary | Hard | 拓扑排序 |
| 212 | Word Search II | Hard | DFS + Trie |

### 代码模板

```python
# Number of Islands (LeetCode 200) - DFS 淹没
def numIslands(grid):
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return
        if grid[i][j] != '1': return
        grid[i][j] = '0'      # 标记已访问
        for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            dfs(i+di, j+dj)
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count

# 拓扑排序 DFS (课程表检测环)
def canFinish(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    for a, b in prerequisites:
        graph[b].append(a)
    
    # 0=未访问, 1=访问中(在栈上), 2=已完成
    state = [0] * numCourses
    
    def dfs(node):
        if state[node] == 1: return False  # 发现环
        if state[node] == 2: return True   # 已处理
        state[node] = 1
        for nei in graph[node]:
            if not dfs(nei): return False
        state[node] = 2
        return True
    
    return all(dfs(i) for i in range(numCourses))

# Tarjan 桥检测 (LeetCode 1192) - 核心模板
def criticalConnections(n, connections):
    graph = [[] for _ in range(n)]
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)
    
    disc = [-1] * n
    low = [-1] * n
    timer = [0]
    bridges = []
    
    def dfs(u, parent):
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        for v in graph[u]:
            if v == parent: continue
            if disc[v] == -1:       # 树边
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:   # v 无法回到 u 的祖先 → 桥
                    bridges.append([u, v])
            else:                   # 回边
                low[u] = min(low[u], disc[v])
    
    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)
    return bridges
```

---

## 12. 图 - 拓扑排序

### 核心思路
- **Kahn 算法（BFS）**：维护入度数组，入度为 0 的先处理
- **DFS 后序**：DFS 完成后逆序即为拓扑序
- 检测环：Kahn 中最终处理节点数 < 总节点数

### 代表题目

| 题号 | 题目 | 难度 |
|------|------|------|
| 207 | Course Schedule | Medium |
| 210 | Course Schedule II | Medium |
| 269 | Alien Dictionary | Hard |
| 1462 | Course Schedule IV | Medium |

### 代码模板

```python
from collections import deque, defaultdict

# Kahn 算法 BFS 拓扑排序
def topologicalSort(numNodes, edges):
    """
    edges: [(a, b)] 表示 b → a（b 是 a 的前置）
    """
    graph = defaultdict(list)
    indegree = [0] * numNodes
    
    for a, b in edges:
        graph[b].append(a)
        indegree[a] += 1
    
    queue = deque([i for i in range(numNodes) if indegree[i] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    
    # 若 len(result) == numNodes：无环；否则有环
    return result if len(result) == numNodes else []

# DFS 拓扑排序（Alien Dictionary）
def alienOrder(words):
    # 建图：比较相邻单词找字符顺序
    graph = defaultdict(set)
    all_chars = set(c for w in words for c in w)
    
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        if len(w1) > len(w2) and w1[:len(w2)] == w2:
            return ""   # 无效
        for a, b in zip(w1, w2):
            if a != b:
                graph[a].add(b)
                break
    
    state = {}   # 0=未访问, 1=访问中, 2=已完成
    result = []
    
    def dfs(c):
        if c in state:
            return state[c] != 1  # 1=环
        state[c] = 1
        for nei in graph[c]:
            if not dfs(nei): return False
        state[c] = 2
        result.append(c)
        return True
    
    for c in all_chars:
        if not dfs(c): return ""
    
    return "".join(reversed(result))
```

---

## 13. 前缀积/前缀和

### 核心思路
- 预处理 `prefix[i]` = 前 i 个元素的乘积/和
- 后缀类似，或从右到左扫一遍
- `result[i] = prefix[i] * suffix[i+1]`

### 代表题目

| 题号 | 题目 | 难度 |
|------|------|------|
| 238 | Product of Array Except Self | Medium |
| 304 | Range Sum Query 2D | Medium |

### 代码模板

```python
# Product of Array Except Self (LeetCode 238) - O(n) 时间，O(1) 空间
def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n
    
    # 先算左前缀积
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]
    
    # 再乘右后缀积
    right = 1
    for i in range(n-1, -1, -1):
        result[i] *= right
        right *= nums[i]
    
    return result
```

---

## 14. 排列与下一个排列

### 核心思路（Next Permutation 标准三步）
1. 从右向左找第一个**下降点** `i`（`nums[i] < nums[i+1]`）
2. 从右向左找第一个**比 `nums[i]` 大的数** `j`，交换 `nums[i]` 和 `nums[j]`
3. 将 `nums[i+1:]` 反转（变为最小排列）
4. 特例：若没有下降点（已是最大排列），整体反转

### 代表题目

| 题号 | 题目 | 难度 |
|------|------|------|
| 31 | Next Permutation | Medium |
| 556 | Next Greater Element III | Medium |

### 代码模板

```python
# Next Permutation (LeetCode 31)
def nextPermutation(nums):
    n = len(nums)
    # Step 1: 从右找下降点 i
    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            # Step 2: 从右找比 nums[i] 大的数 j
            for j in range(n-1, i, -1):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    # Step 3: 反转 i+1 之后的部分
                    nums[i+1:] = reversed(nums[i+1:])
                    return
    # 已是最大排列，整体反转
    nums[:] = nums[::-1]

# Next Greater Element III (LeetCode 556) - 数字版
def nextGreaterElement(n):
    digits = list(map(int, str(n)))
    length = len(digits)
    for i in range(length-2, -1, -1):
        if digits[i] < digits[i+1]:
            for j in range(length-1, i, -1):
                if digits[i] < digits[j]:
                    digits[i], digits[j] = digits[j], digits[i]
                    digits[i+1:] = reversed(digits[i+1:])
                    result = int("".join(map(str, digits)))
                    return result if result <= 2**31 - 1 else -1
    return -1
```

---

## 15. 位运算 / 快速幂

### 核心思路
- **快速幂**：每次平方，二进制分解指数，O(log n)
- **不用除法做除法**：用位移模拟，每次让 divisor 翻倍

### 代表题目

| 题号 | 题目 | 难度 |
|------|------|------|
| 50 | Pow(x, n) | Medium |
| 29 | Divide Two Integers | Medium |

### 代码模板

```python
# 快速幂 (LeetCode 50)
def myPow(x, n):
    if n < 0:
        x, n = 1/x, -n
    result = 1
    while n:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2
    return result

# 整数除法（不用 * / %）(LeetCode 29)
def divide(dividend, divisor):
    INT_MAX, INT_MIN = 2**31 - 1, -2**31
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX      # 溢出处理
    
    negative = (dividend < 0) ^ (divisor < 0)
    a, b = abs(dividend), abs(divisor)
    
    quotient = 0
    while a >= b:
        tmp, mult = b, 1
        while a >= (tmp << 1):
            tmp <<= 1
            mult <<= 1
        a -= tmp
        quotient += mult
    
    return -quotient if negative else quotient
```

---

## 16. 数学 / 几何

### 代表题目

| 题号 | 题目 | 难度 | 技巧 |
|------|------|------|------|
| 149 | Max Points on a Line | Hard | 斜率用最简分数表示，避免浮点误差 |

### 代码模板

```python
from math import gcd
from collections import defaultdict

# Max Points on a Line (LeetCode 149)
def maxPoints(points):
    n = len(points)
    if n <= 2: return n
    
    result = 0
    for i in range(n):
        slope_count = defaultdict(int)
        for j in range(n):
            if i == j: continue
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            g = gcd(abs(dx), abs(dy))
            # 规范化斜率（处理 gcd=0 的特殊情况）
            key = (dx // g, dy // g) if g != 0 else (0, 0)
            slope_count[key] += 1
            result = max(result, slope_count[key])
    
    return result + 1  # +1 是基准点本身
```

---

## 17. 区间排序

### 核心思路
- 先按 `start` 排序
- 判断重叠：`前一个的 end > 当前的 start`（严格大于）

### 代表题目

| 题号 | 题目 | 难度 |
|------|------|------|
| 252 | Meeting Rooms | Easy |
| 56 | Merge Intervals | Medium |
| 57 | Insert Interval | Medium |

### 代码模板

```python
# 判断是否有区间重叠 (LeetCode 252)
def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])
    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i+1][0]:
            return False
    return True

# 合并区间 (LeetCode 56)
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= result[-1][1]:   # 重叠
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])
    return result
```

---

## 18. 字典树 Trie

### 核心思路
- 每个节点代表一个字符，路径代表前缀
- 与 DFS 配合，用于单词搜索（Word Search II）
- **关键优化**：DFS 过程中若当前前缀不在 Trie 中则提前剪枝

### 代表题目

| 题号 | 题目 | 难度 |
|------|------|------|
| 212 | Word Search II | Hard |

### 代码模板

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   # 完整单词（仅叶节点非 None）

def buildTrie(words):
    root = TrieNode()
    for word in words:
        node = root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = word
    return root

# Word Search II (LeetCode 212) - DFS + Trie
def findWords(board, words):
    root = buildTrie(words)
    m, n = len(board), len(board[0])
    result = set()
    
    def dfs(i, j, node):
        c = board[i][j]
        if c not in node.children: return
        next_node = node.children[c]
        if next_node.word:
            result.add(next_node.word)
            next_node.word = None   # 避免重复添加
        
        board[i][j] = '#'   # 标记访问
        for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < m and 0 <= nj < n:
                dfs(ni, nj, next_node)
        board[i][j] = c     # 恢复
    
    for i in range(m):
        for j in range(n):
            dfs(i, j, root)
    
    return list(result)
```

---

## 🔑 常见面试题型速查

### 题型识别口诀

| 题目特征 | 优先考虑 |
|----------|----------|
| 「连续子数组/子串」 | 滑动窗口 |
| 「有序数组找两个数」 | 双指针对撞 |
| 「链表环/中点/合并」 | 快慢指针 |
| 「K 路有序合并/前 K 小」 | 最小堆 |
| 「括号合法/下一个更大」 | 栈 |
| 「二维路径计数/最值」 | 网格 DP |
| 「两个字符串的公共/变换」 | 字符串 DP |
| 「单字符串的子序列/回文」 | 区间 DP |
| 「图中连通性/路径」 | DFS/BFS |
| 「有依赖关系的排序」 | 拓扑排序 |
| 「字符串前缀匹配/多词搜索」 | Trie + DFS |
| 「下一个排列/最小字典序」 | 标准三步法 |

### DP 初始化速查

```
dp[0][j] = j        → Edit Distance（插入 j 个字符）
dp[i][0] = i        → Edit Distance（删除 i 个字符）
dp[i][0] = 1        → Distinct Subsequences（t 为空，方案数 1）
dp[0][0] = True     → Wildcard/Regex/Interleave（两串均空，匹配成功）
dp[i][i] = 1        → 区间 DP（单字符是长度 1 的回文）
```

### 复杂度速查表

| 算法 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| 双指针 | O(n) | O(1) |
| 滑动窗口 | O(n) | O(k) |
| K 路归并 (堆) | O(N log k) | O(k) |
| 字符串 DP | O(m×n) | O(m×n) |
| 区间 DP | O(n³) | O(n²) |
| 拓扑排序 (Kahn) | O(V+E) | O(V+E) |
| Tarjan 桥 | O(V+E) | O(V+E) |
| 快速幂 | O(log n) | O(1) |

---

*最后更新：2026-03-25*

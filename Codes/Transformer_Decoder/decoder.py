"""
Transformer 架构 - Encoder-Decoder vs Decoder-Only
===================================================

包含两种架构的简洁实现 (PyTorch版本)
"""

import torch
import torch.nn as nn
import math


class Attention(nn.Module):
    """缩放点积注意力"""
    
    def forward(self, Q, K, V, mask=None):
        """
        Args:
            Q, K, V: shape (batch, num_heads, seq_len, d_k)
            mask: Causal mask, shape (seq_len, seq_len)
        
        Returns:
            output: (batch, num_heads, seq_len, d_k)
            attention_weights: (batch, num_heads, seq_len, seq_len)
        """
        d_k = Q.shape[-1]
        
        # 计算相似度
        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)
        
        # 应用 mask
        if mask is not None:
            scores = scores.masked_fill(mask == 0, float('-inf'))
        
        # Softmax 归一化
        attention_weights = torch.softmax(scores, dim=-1)
        
        # 加权求和
        output = torch.matmul(attention_weights, V)
        
        return output, attention_weights


class MultiHeadAttention(nn.Module):
    """多头注意力"""
    
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        
        assert d_model % num_heads == 0, "d_model must be divisible by num_heads"
        
        # 线性投影层
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)
        
        self.attention = Attention()
    
    def split_heads(self, x):
        """(batch, seq_len, d_model) -> (batch, num_heads, seq_len, d_k)"""
        batch_size, seq_len, _ = x.shape
        x = x.reshape(batch_size, seq_len, self.num_heads, self.d_k)
        return x.transpose(1, 2)
    
    def combine_heads(self, x):
        """(batch, num_heads, seq_len, d_k) -> (batch, seq_len, d_model)"""
        batch_size, _, seq_len, _ = x.shape
        x = x.transpose(1, 2)
        return x.reshape(batch_size, seq_len, self.d_model)
    
    def forward(self, Q, K, V, mask=None, kv_cache=None, return_cache=False):
        """
        Args:
            Q, K, V: shape (batch, seq_len, d_model)
            mask: Causal mask
            kv_cache: None or {'K': ..., 'V': ...} 用于 KV Cache
            return_cache: 是否返回缓存供下一步使用
        
        Returns:
            如果 return_cache=False: output (batch, seq_len, d_model)
            如果 return_cache=True: (output, cache_dict)
        """
        batch_size = Q.shape[0]
        
        # 线性变换
        Q = self.W_q(Q)
        K = self.W_k(K)
        V = self.W_v(V)
        
        # 分头
        Q = self.split_heads(Q)  # (batch, num_heads, seq_len, d_k)
        K = self.split_heads(K)
        V = self.split_heads(V)
        
        # ===== KV Cache 逻辑 =====
        if kv_cache is not None:
            # 使用 KV Cache：拼接历史缓存
            K_cached = kv_cache['K']  # (batch, num_heads, old_len, d_k)
            V_cached = kv_cache['V']
            
            # 拼接新 K,V（这是 KV Cache 加速的关键）
            K = torch.cat([K_cached, K], dim=2)  # (batch, num_heads, old_len+new_len, d_k)
            V = torch.cat([V_cached, V], dim=2)
            
            # 需要调整 mask 来适应新的 K,V 长度
            if mask is not None:
                # 只保留最后一行（新 token 只能看到所有历史）
                mask = mask[-1:, :]  # (1, seq_len) 最后一行
        
        # 计算注意力
        output, _ = self.attention(Q, K, V, mask)
        
        # 合并头
        output = self.combine_heads(output)
        
        # 输出线性变换
        output = self.W_o(output)
        
        # 返回输出和缓存
        if return_cache:
            return output, {'K': K, 'V': V}
        else:
            return output


# ============================================================================
# 1. Encoder-Decoder 架构
# ============================================================================

class EncoderDecoderAttention(nn.Module):
    """
    Encoder-Decoder 架构 - Decoder 部分
    
    包含：
    1. Self-Attention (有 Causal Mask)
    2. Cross-Attention (连接 Encoder)
    """
    
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.d_model = d_model
        self.num_heads = num_heads
        
        self.self_attention = MultiHeadAttention(d_model, num_heads)
        self.cross_attention = MultiHeadAttention(d_model, num_heads)
    
    def create_causal_mask(self, seq_len):
        """创建因果掩码"""
        mask = torch.tril(torch.ones(seq_len, seq_len))
        return mask
    
    def forward(self, decoder_input, encoder_output):
        """
        Args:
            decoder_input: (batch, seq_len_decoder, d_model)
            encoder_output: (batch, seq_len_encoder, d_model)
        """
        seq_len = decoder_input.shape[1]
        
        # 1. Self-Attention with Causal Mask
        causal_mask = self.create_causal_mask(seq_len)
        self_attn_output = self.self_attention(
            Q=decoder_input,
            K=decoder_input,
            V=decoder_input,
            mask=causal_mask
        )
        
        # 2. Cross-Attention (Q from Decoder, K,V from Encoder)
        cross_attn_output = self.cross_attention(
            Q=self_attn_output,
            K=encoder_output,
            V=encoder_output,
            mask=None
        )
        
        return cross_attn_output


# ============================================================================
# 2. Decoder-Only 架构 (GPT 风格)
# ============================================================================

class DecoderOnlyAttention(nn.Module):
    """
    Decoder-Only 架构 - GPT 风格
    
    只有堆叠的 Self-Attention 层，所有信息来自输入序列本身
    应用：GPT, GPT-2, ChatGPT 等
    """
    
    def __init__(self, d_model, num_heads, num_layers=6):
        super().__init__()
        self.d_model = d_model
        self.num_heads = num_heads
        self.num_layers = num_layers
        
        self.attention_layers = nn.ModuleList([
            MultiHeadAttention(d_model, num_heads) for _ in range(num_layers)
        ])
    
    def create_causal_mask(self, seq_len):
        """创建因果掩码"""
        mask = torch.tril(torch.ones(seq_len, seq_len))
        return mask
    
    def forward(self, input_sequence, kv_cache=None, use_cache=False):
        """
        Args:
            input_sequence: 输入序列，形状 (batch, seq_len, d_model)
            kv_cache: None 或 [{'K': ..., 'V': ...}, ...]（每层一个）
            use_cache: 是否使用/返回 KV Cache
        
        Returns:
            output: 形状 (batch, seq_len, d_model)
            new_kv_cache: 如果 use_cache=True，返回更新后的缓存
        """
        seq_len = input_sequence.shape[1]
        causal_mask = self.create_causal_mask(seq_len)
        
        x = input_sequence
        new_kv_cache = [] if use_cache else None
        
        # 堆叠多层 Self-Attention（每层都使用 Causal Mask）
        for layer_idx, layer in enumerate(self.attention_layers):
            # 获取当前层的缓存（如果使用）
            layer_cache = kv_cache[layer_idx] if (kv_cache is not None) else None
            
            # 前向传播
            result = layer(
                Q=x,
                K=x,
                V=x,
                mask=causal_mask,
                kv_cache=layer_cache,
                return_cache=use_cache
            )
            
            # 处理返回值（有缓存时返回 tuple，无缓存时返回 tensor）
            if use_cache:
                x, updated_cache = result
                new_kv_cache.append(updated_cache)
            else:
                x = result
        
        if use_cache:
            return x, new_kv_cache
        else:
            return x


class DecoderOnlyInference(nn.Module):
    """
    Decoder-Only 推理
    
    支持两种模式：
    1. 无 KV Cache（use_cache=False）：每步重新处理整个序列，计算量 O(N²) per step
    2. 使用 KV Cache（use_cache=True）：缓存历史 K,V，只处理新 token，计算量 O(1) per step
    
    通过 use_cache 参数控制 MultiHeadAttention 的缓存行为
    """
    
    def __init__(self, d_model, num_heads, num_layers=3, vocab_size=1000, max_len=100, use_cache=True):
        super().__init__()
        self.d_model = d_model
        self.num_heads = num_heads
        self.vocab_size = vocab_size
        self.max_len = max_len
        self.use_cache = use_cache
        
        self.model = DecoderOnlyAttention(d_model, num_heads, num_layers)
        self.output_projection = nn.Linear(d_model, vocab_size)
    
    def generate(self, start_token, end_token=2):
        """
        自回归生成 Token
        
        Args:
            start_token: 开始 token ID
            end_token: 结束 token ID
        
        Returns:
            生成的 token 序列（不包括 start_token）
        """
        tokens = [start_token]
        kv_cache = None  # 初始化缓存为 None
        
        with torch.no_grad():
            for step in range(self.max_len):
                if self.use_cache:
                    # ===== 使用 KV Cache 模式 =====
                    if step == 0:
                        # Prefill 阶段：处理完整开始 token
                        input_seq = self._tokens_to_embedding(tokens)  # (batch, 1, d_model)
                    else:
                        # Decode 阶段：只处理新 token
                        input_seq = self._tokens_to_embedding([tokens[-1]])  # (batch, 1, d_model)
                    
                    # 前向传播，使用缓存
                    output, kv_cache = self.model(
                        input_seq,
                        kv_cache=kv_cache,
                        use_cache=True
                    )
                else:
                    # ===== 不使用 KV Cache 模式 =====
                    # 每步都处理完整序列
                    input_seq = self._tokens_to_embedding(tokens)
                    output = self.model(input_seq, use_cache=False)
                
                # 提取最后一个位置的隐向量，预测下一个 token
                last_hidden = output[:, -1, :]
                logits = self.output_projection(last_hidden)
                probs = torch.softmax(logits, dim=-1)
                next_token = torch.argmax(probs, dim=-1)[0].item()
                
                tokens.append(next_token)
                if next_token == end_token:
                    break
        
        return tokens[1:]  # 去掉 start_token
    
    def _tokens_to_embedding(self, token_ids):
        """将 token IDs 转换为 embedding（模拟）"""
        batch_size = 1
        seq_len = len(token_ids)
        return torch.randn(batch_size, seq_len, self.d_model) * 0.1


# ============================================================================
# 演示和测试
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("Transformer 架构演示 (PyTorch 版本)")
    print("=" * 80)
    
    # 参数
    d_model = 64
    num_heads = 4
    start_token = 1
    end_token = 2
    
    # ========== 1. Encoder-Decoder 架构 ==========
    print(f"\n【1. Encoder-Decoder 架构 - 前向传播】")
    
    ed_model = EncoderDecoderAttention(d_model, num_heads)
    decoder_input = torch.randn(1, 5, d_model) * 0.01
    encoder_output = torch.randn(1, 6, d_model) * 0.01
    
    ed_output = ed_model(decoder_input, encoder_output)
    print(f"Encoder-Decoder 输出: {ed_output.shape}")
    
    causal_mask = ed_model.create_causal_mask(5)
    print(f"Causal Mask:\n{causal_mask.int()}")
    
    # ========== 2. Decoder-Only 前向传播 ==========
    print(f"\n【2. Decoder-Only 架构 - 前向传播】")
    
    do_model = DecoderOnlyAttention(d_model, num_heads, num_layers=3)
    input_seq = torch.randn(1, 5, d_model) * 0.01
    do_output = do_model(input_seq)
    print(f"Decoder-Only 输出: {do_output.shape}")
    
    # ========== 3. Decoder-Only 推理 - 无 KV Cache ==========
    print(f"\n【3. Decoder-Only 推理 - 无 KV Cache】")
    
    inference_no_cache = DecoderOnlyInference(
        d_model=d_model,
        num_heads=num_heads,
        num_layers=3,
        vocab_size=1000,
        max_len=8,
        use_cache=False
    )
    
    generated_no_cache = inference_no_cache.generate(start_token, end_token)
    print(f"生成的 token: {generated_no_cache}")
    print(f"总长度: {len(generated_no_cache)}")
    print(f"复杂度: O(N²) - 每步都重新处理完整序列")
    
    # ========== 4. Decoder-Only 推理 - 使用 KV Cache ==========
    print(f"\n【4. Decoder-Only 推理 - 使用 KV Cache】")
    
    inference_with_cache = DecoderOnlyInference(
        d_model=d_model,
        num_heads=num_heads,
        num_layers=3,
        vocab_size=1000,
        max_len=8,
        use_cache=True
    )
    
    generated_with_cache = inference_with_cache.generate(start_token, end_token)
    print(f"生成的 token: {generated_with_cache}")
    print(f"总长度: {len(generated_with_cache)}")
    print(f"复杂度: O(N) - 使用缓存，只处理新 token")
    
    # ========== 5. 架构对比 ==========
    print(f"\n【5. 架构对比】")
    print(f"\nEncoder-Decoder:")
    print(f"  • 需要 Encoder 处理输入")
    print(f"  • Decoder 有 Self-Attention + Cross-Attention")
    print(f"  • 应用: 翻译、摘要、问答")
    
    print(f"\nDecoder-Only:")
    print(f"  • 只有 Self-Attention 层")
    print(f"  • 推理时使用 KV Cache 加速")
    print(f"  • 应用: GPT, ChatGPT, 文本生成")
    
    print(f"\n【Decoder-Only 推理对比】")
    print(f"\n无 KV Cache:")
    print(f"  Step 1: 处理 [1]       → 1 个 token")
    print(f"  Step 2: 处理 [1, tok1] → 2 个 token")
    print(f"  Step 3: 处理 [1, tok1, tok2] → 3 个 token")
    print(f"  总计: 1+2+3+...+N = O(N²)")
    
    print(f"\n使用 KV Cache:")
    print(f"  Step 1: 处理 [1]，缓存 K,V")
    print(f"  Step 2: 处理 [tok1]，重用缓存")
    print(f"  Step 3: 处理 [tok2]，重用缓存")
    print(f"  总计: 1+1+1+...+1 = O(N) ✓")
    
    print("\n" + "=" * 80)
    print("演示完成！")

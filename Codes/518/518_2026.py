"""
[518] Coin Change 2
https://leetcode.com/problems/coin-change-2/

You are given an integer array coins representing coins of different denominations and an integer
amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made
up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:
    Input: amount = 5, coins = [1,2,5]
    Output: 4
    Explanation: There are four ways to make 5:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1

Example 2:
    Input: amount = 3, coins = [10]
    Output: 0
    Explanation: The amount of 3 cannot be made up just with coins of 10.

Example 3:
    Input: amount = 10, coins = [10]
    Output: 1
    Explanation: The amount of 10 can be made up only in one way: 10=10.

Constraints:
    - 1 <= coins.length <= 300
    - 1 <= coins[i] <= 5000
    - 0 <= amount <= 5000
"""


def change(amount, coins):
    """
    Return the number of combinations that make up the given amount.
    
    Core Idea: This is an Unbounded Knapsack problem.
    
    Key Difference from LeetCode 416:
    - 416: Can we make the sum? (Boolean, each number used ≤ 1 time)
    - 518: How many ways to make the sum? (Count, each coin used unlimited times)
    
    Hint:
    - Use DP: dp[i] = number of ways to make amount i
    - Iterate coins in outer loop, amounts in inner loop (opposite of 416!)
    - This ensures we count combinations, not permutations
    
    Important: Why iterate coins first?
    - If we iterate amount first, we'll count [1,2] and [2,1] as different ways
    - By iterating coins first, we ensure each combination is counted only once
    """
    # 🔴 问题 1：必须初始化 dp[0] = 1
    dp = [0] * (amount + 1)
    dp[0] = 1  # 凑出 0 元只有一种方式：不选任何硬币
    
    # 🔴 问题 2：不需要提前初始化 dp[coin]
    # 直接在主循环中处理，这样既避免重复计数，又支持无限次使用
    
    # 主循环：先遍历 coins，再遍历 amount
    for coin in coins:
        # 从前向后遍历 amount（与 416 的从后向前相反！）
        for i in range(coin, amount + 1):
            # 加上用这个 coin 的方式数
            dp[i] += dp[i - coin]
    
    return dp[amount]


def change_detailed_explanation(amount, coins):
    """
    === 详细讲解版本 ===
    
    让我们用一个例子来理解这道题：
    amount = 5, coins = [1, 2, 5]
    
    问题：用硬币 [1, 2, 5] 凑出 5 元，有多少种方式？
    
    答案应该是：
    1. [5]           → 直接用 5 元硬币
    2. [2, 2, 1]     → 两个 2 元 + 一个 1 元
    3. [2, 1, 1, 1]  → 一个 2 元 + 三个 1 元
    4. [1, 1, 1, 1, 1] → 五个 1 元
    
    所以答案 = 4
    
    ===== DP 状态定义 =====
    dp[i] = 凑出 i 元的方案数
    
    初始状态：
    dp[0] = 1   (凑出 0 元：不选任何硬币，1 种方式)
    dp[1] = 0   (还没处理，暂时 0 种)
    dp[2] = 0
    dp[3] = 0
    dp[4] = 0
    dp[5] = 0
    
    ===== 关键：为什么要 coins 在外层，amount 在内层？=====
    
    如果 amount 在外层（错误的方式）：
    ────────────────────────
    外层遍历 amount: 1→5
      内层遍历 coin: 遍历所有硬币
      
    这样会导致统计排列(Permutation)而不是组合(Combination)
    比如 [1,2] 和 [2,1] 会被统计为两种不同的方式
    
    
    如果 coins 在外层（正确的方式）：
    ────────────────────────────────
    外层遍历 coin: 依次处理硬币 1 → 2 → 5
      内层遍历 amount: 1→5
    
    这样每个硬币只"加入"一次，避免了排列的重复计数
    
    ===== 详细过程（coins 在外层）=====
    
    【处理硬币 coin = 1】
    ─────────────────────
    初始：dp = [1, 0, 0, 0, 0, 0]
    
    循环 i = 1: dp[1] += dp[1-1] = dp[1] + dp[0] = 0 + 1 = 1
               dp = [1, 1, 0, 0, 0, 0]
    
    循环 i = 2: dp[2] += dp[2-1] = dp[2] + dp[1] = 0 + 1 = 1
               dp = [1, 1, 1, 0, 0, 0]
    
    循环 i = 3: dp[3] += dp[3-1] = dp[3] + dp[2] = 0 + 1 = 1
               dp = [1, 1, 1, 1, 0, 0]
    
    循环 i = 4: dp[4] += dp[4-1] = dp[4] + dp[3] = 0 + 1 = 1
               dp = [1, 1, 1, 1, 1, 0]
    
    循环 i = 5: dp[5] += dp[5-1] = dp[5] + dp[4] = 0 + 1 = 1
               dp = [1, 1, 1, 1, 1, 1]
    
    【现在只用硬币 [1] 的结论】
    dp[5] = 1  → 只能凑出 [1,1,1,1,1]
    
    
    【处理硬币 coin = 2】
    ─────────────────────
    初始：dp = [1, 1, 1, 1, 1, 1]
    
    循环 i = 2: dp[2] += dp[2-2] = dp[2] + dp[0] = 1 + 1 = 2
               dp = [1, 1, 2, 1, 1, 1]
               💡 现在有 2 种方式凑出 2 元：[1,1] 和 [2]
    
    循环 i = 3: dp[3] += dp[3-2] = dp[3] + dp[1] = 1 + 1 = 2
               dp = [1, 1, 2, 2, 1, 1]
               💡 现在有 2 种方式凑出 3 元：[1,1,1] 和 [2,1]
    
    循环 i = 4: dp[4] += dp[4-2] = dp[4] + dp[2] = 1 + 2 = 3
               dp = [1, 1, 2, 2, 3, 1]
               💡 现在有 3 种方式凑出 4 元：[1,1,1,1], [2,1,1], [2,2]
    
    循环 i = 5: dp[5] += dp[5-2] = dp[5] + dp[3] = 1 + 2 = 3
               dp = [1, 1, 2, 2, 3, 3]
               💡 现在有 3 种方式凑出 5 元：[1,1,1,1,1], [2,1,1,1], [2,2,1]
    
    【现在用硬币 [1,2] 的结论】
    dp[5] = 3
    
    
    【处理硬币 coin = 5】
    ─────────────────────
    初始：dp = [1, 1, 2, 2, 3, 3]
    
    循环 i = 5: dp[5] += dp[5-5] = dp[5] + dp[0] = 3 + 1 = 4
               dp = [1, 1, 2, 2, 3, 4]
               💡 现在有 4 种方式凑出 5 元：
                  - [1,1,1,1,1]
                  - [2,1,1,1]
                  - [2,2,1]
                  - [5]
    
    【最终结论】
    dp[5] = 4 ✓
    
    ===== 关键洞察 =====
    
    为什么这样能避免排列？
    ────────────────────
    因为我们是"依次加入"每个硬币类型。
    
    当处理硬币 coin=1 时，所有结果都是只用 [1] 的方案
    当处理硬币 coin=2 时，我们基于之前的结果加上新的 [2] 的方案
    当处理硬币 coin=5 时，我们基于之前的结果加上新的 [5] 的方案
    
    这样做的结果就是：
    - 不会产生 [1,2] 和 [2,1] 这样的排列重复
    - 只会产生 [1,2] 或 [2,1] 中的一个
    
    对比错误的方式（amount在外层）：
    ──────────────────────────────
    如果先固定 amount=5，然后遍历所有硬币，会这样：
    - 先用 coin=1，凑出 [1,1,1,1,1]
    - 再用 coin=2，凑出 [2,1,1,1], [2,2,1] 等
    - 再用 coin=5，凑出 [5]
    
    但是当内层再次循环时，会反复更新相同的金额
    最终导致同时计算了 [1,2] 和 [2,1]
    
    ===== 总结 =====
    
    ✓ coins 在外层 → 组合计数（去重）
    ✗ amount 在外层 → 排列计数（有重复）
    """
    
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    print(f"\n初始 DP: {dp}\n")
    
    for coin_idx, coin in enumerate(coins):
        print(f"【处理硬币 coin = {coin}】")
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
            print(f"  dp[{i}] += dp[{i}-{coin}] = dp[{i}] ({dp[i]})")
        print(f"  处理完后: dp = {dp}\n")
    
    return dp[amount]

# Test cases
if __name__ == "__main__":
    test_cases = [
        (5, [1, 2, 5], 4),      # [5], [2,2,1], [2,1,1,1], [1,1,1,1,1]
        (3, [10], 0),           # Cannot make 3 with coin 10
        (10, [10], 1),          # [10]
        (0, [1], 1),            # Empty selection
        (1, [1, 2], 1),         # [1]
        (2, [1, 2], 2),         # [2], [1,1]
        (5, [2], 0),            # Cannot make 5 with only coin 2
        (4, [1, 2, 3], 4),      # [3,1], [2,2], [2,1,1], [1,1,1,1]
        (5, [1, 2], 3),         # [2,2,1], [2,1,1,1], [1,1,1,1,1]
    ]
    
    print("=" * 70)
    print("LeetCode 518 - Coin Change 2")
    print("=" * 70)
    
    for amount, coins, expected in test_cases:
        try:
            result = change(amount, coins)
            if result is None:
                print(f"⚠️  amount={amount}, coins={coins} -> Not implemented")
            else:
                is_correct = result == expected
                status = "✓" if is_correct else "✗"
                print(f"{status} amount={amount}, coins={coins}")
                print(f"   Output: {result}, Expected: {expected}")
        except Exception as e:
            print(f"❌ amount={amount}, coins={coins} -> Error: {e}")

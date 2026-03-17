"""
[322] Coin Change
https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations and an integer
amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money
cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
    Input: coins = [1,2,5], amount = 5
    Output: 1
    Explanation: 5 = 5 (uses 1 coin, which is optimal)

Example 2:
    Input: coins = [2], amount = 3
    Output: -1
    Explanation: The amount 3 cannot be made up by coins of denomination 2.

Example 3:
    Input: coins = [10], amount = 10
    Output: 1
    Explanation: 10 = 10, uses 1 coin

Constraints:
    - 1 <= coins.length <= 12
    - 1 <= coins[i] <= 2^31 - 1
    - 0 <= amount <= 10^4
"""


def coinChange(coins, amount):
    """
    Return the fewest number of coins needed to make up the amount.
    
    Core Idea: This is a DP problem, but different from Coin Change 2 (LeetCode 518)
    
    Difference from LeetCode 518:
    - 518: How many COMBINATIONS to make the amount? (return count)
    - 322: What is the MINIMUM NUMBER OF COINS? (return fewest count)
    
    State Transition: dp[i] = min(dp[i], dp[i - coin] + 1)
    
    Why use infinity for initialization?
    - dp[0] = 0     (base case: 0 coins for amount 0)
    - dp[i] = inf   (not yet computed, means unreachable)
    - If final dp[amount] == inf → return -1 (impossible)
    - This way we can distinguish "unreachable" from "requires 0 coins"
    
    Key: Single loop for all coins and amounts
    """
    # 🔑 Initialize with infinity
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins for amount 0
    
    # Process each coin and update all reachable amounts
    for coin in coins:
        for i in range(coin, amount + 1):
            # Try adding this coin to make amount i
            if dp[i - coin] != float('inf'):  # Can only add if (i-coin) is reachable
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return result or -1 if impossible
    print(dp)
    return dp[amount] if dp[amount] != float('inf') else -1


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 5], 5, 1),      # [5] → 1 coin (optimal)
        ([2], 3, -1),           # Impossible
        ([10], 10, 1),          # [10] → 1 coin
        ([1], 0, 0),            # 0 coins needed for 0 amount
        ([2, 5], 7, 2),         # [5, 2] → 2 coins (optimal)
        ([1, 2, 5], 11, 3),     # [5, 5, 1] → 3 coins (optimal)
        ([3, 4], 7, 2),         # [3, 4] → 2 coins (optimal)
        ([2], 1, -1),           # Impossible
        ([1], 10, 10),          # [1]*10 → 10 coins
        ([1, 3, 4], 6, 2),      # [3, 3] → 2 coins (optimal)
    ]
    
    print("=" * 70)
    print("LeetCode 322 - Coin Change")
    print("=" * 70)
    
    for coins, amount, expected in test_cases:
        try:
            result = coinChange(coins, amount)
            if result is None:
                print(f"⚠️  coins={coins}, amount={amount} -> Not implemented")
            else:
                is_correct = result == expected
                status = "✓" if is_correct else "✗"
                print(f"{status} coins={coins}, amount={amount}")
                print(f"   Output: {result}, Expected: {expected}")
        except Exception as e:
            print(f"❌ coins={coins}, amount={amount} -> Error: {e}")

"""
[416] Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/

Given an integer array nums, return true if you can partition the array into two subsets such that
the sum of elements in both subsets is equal or false otherwise.

Example 1:
    Input: nums = [1,5,11,5]
    Output: true

Example 2:
    Input: nums = [2,2,1,1]
    Output: true

Example 3:
    Input: nums = [1,2,5]
    Output: false

Constraints:
    - 1 <= nums.length <= 200
    - 1 <= nums[i] <= 100
"""


def canPartition(nums):
    """
    Determine if array can be partitioned into two equal sum subsets.
    
    Core Idea: Can we find a subset with sum = total_sum / 2?
    This is a 0/1 Knapsack problem.
    
    Hint:
    - Check if total sum is odd
    - Use DP: dp[i] = True means we can make sum equal to i
    - Iterate through nums and update dp backwards
    """
    total_sum = sum(nums)
    
    # 🔴 问题 1：需要检查总和的奇偶性
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    
    # 🔴 问题 2：DP 数组大小应该是 target + 1，不是 total_sum + 1
    dp = [False] * (target + 1)
    dp[0] = True  # 基础情况：能凑出 0（不选任何元素）
    
    # 🔴 问题 3：不需要提前初始化 dp[num]，在主循环中会处理
    for num in nums:
        # 从后向前遍历，避免同一个数字用两次
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    # print(dp)
    return dp[target]



# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 5, 11, 5], True),
        ([2, 2, 1, 1], True),
        ([1, 2, 5], False),
        ([1, 2, 3, 4], True),
        ([2], False),
        ([1, 1], True),
        ([1, 2, 3, 5], False),
        ([3, 3, 3, 4, 5], True),
    ]
    
    print("=" * 70)
    print("LeetCode 416 - Partition Equal Subset Sum")
    print("=" * 70)
    
    for nums, expected in test_cases:
        try:
            result = canPartition(nums)
            if result is None:
                print(f"⚠️  nums={nums} -> Not implemented")
            else:
                is_correct = result == expected
                status = "✓" if is_correct else "✗"
                print(f"{status} nums={nums}")
                print(f"   Output: {result}, Expected: {expected}")
        except Exception as e:
            print(f"❌ nums={nums} -> Error: {e}")

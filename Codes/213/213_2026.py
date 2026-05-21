"""
[213] House Robber II
https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street. Each house has a certain amount
of money stashed in it. All houses at this place are arranged in a circle. That means the first
house is the neighbor of the last one. Meanwhile, adjacent houses have a connected security system,
and it will automatically contact the police if two adjacent houses were broken into on the same
night.

Given an integer array nums representing the amount of money of each house, return the maximum
amount of money you can rob tonight without alerting the police.

Example 1:
    Input: nums = [2,3,2]
    Output: 3
    Explanation: You cannot rob house 1 (money = 3) and then rob house 3 (money = 2), because they
    are adjacent houses. You cannot rob house 1 (money = 3) and then rob house 0 (money = 2),
    because they are adjacent houses.

Example 2:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 2) and then rob house 3 (money = 1). Total amount you can rob
    = 2 + 1 = 4.

Example 3:
    Input: nums = [1,2,3]
    Output: 3

Constraints:
    - 1 <= nums.length <= 100
    - 0 <= nums[i] <= 1000
"""


def rob(nums):
    # dp[i] = max(dp[i-j] + num[i], j in range(2, i))
    # 提示（轻量）：环 = 首尾也算邻居。可拆成两类互斥情况分别当成「直线」上的 LC198：
    #   不抢第一家 → 只看 nums[1:]；不抢最后一家 → 只看 nums[:-1]。
    # 两类各自求出的最大可抢金额再取 max；注意 len(nums)==1 时不要对空切片套公式。
    n = len(nums)
    if n == 1:
        return nums[0]

    def subRob(subNums):

        subN = len(subNums)
        if subN == 1:
            return subNums[0]
        if subN == 2:
            return max(subNums[0], subNums[1])

        dp = [0 for _ in range(subN)]
        dp[0] = subNums[0]
        dp[1] = max(subNums[0], subNums[1])
        for i in range(2, subN):
            # for j in range(2, i+1):
            #     dp[i] = max(dp[i], dp[i-j] + subNums[i])
            dp[i] = max(dp[i-1], dp[i-2] + subNums[i])
        # print(dp)
        return dp[subN-1]

    return max(subRob(nums[:-1]), subRob(nums[1:]))


# Test cases
if __name__ == "__main__":
    import traceback

    test_cases = [
        # ([2, 3, 2], 3),
        # ([1, 2, 3, 1], 4),
        # ([1, 2, 3], 3),
        # ([1], 1),
        # ([1, 2], 2),
        # ([0], 0),
        # ([200, 3, 140, 20, 10], 340),
        ([1,2,1,1], 3)
    ]

    print("=" * 70)
    print("LeetCode 213 - House Robber II")
    print("=" * 70)

    for nums, expected in test_cases:
        try:
            result = rob(nums)
            if result is None:
                print(f"[!] nums={nums} -> Not implemented")
            else:
                is_correct = result == expected
                status = "[OK]" if is_correct else "[FAIL]"
                print(f"{status} nums={nums}")
                print(f"   Output: {result}, Expected: {expected}")
        except Exception as e:
            print(f"[ERR] nums={nums} -> {type(e).__name__}: {e}")
            print(traceback.format_exc(), end="")

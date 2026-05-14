"""
[494] Target Sum
https://leetcode.com/problems/target-sum/

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each
integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to
build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.

Example 1:
    Input: nums = [1,1,1,1,1], target = 3
    Output: 5
    Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
    -1 + 1 + 1 + 1 + 1 = 3
    +1 - 1 + 1 + 1 + 1 = 3
    +1 + 1 - 1 + 1 + 1 = 3
    +1 + 1 + 1 - 1 + 1 = 3
    +1 + 1 + 1 + 1 - 1 = 3

Example 2:
    Input: nums = [1], target = 1
    Output: 1

Constraints:
    - 1 <= nums.length <= 20
    - 0 <= nums[i] <= 1000
    - 0 <= sum(nums[i]) <= 1000
    - -1000 <= target <= 1000
"""


def findTargetSumWays_dfs(nums, target):
    
    def dfs(_nums, _idx, _cur, _target):
        if _idx == len(_nums):
            if  _cur == _target:
                return 1
            return 0
        # print(_idx, _cur)
        return dfs(_nums, _idx + 1, _cur + _nums[_idx], _target) + dfs(_nums, _idx + 1, _cur - _nums[_idx], _target)
        
    return dfs(nums, 0, 0, target)


def findTargetSumWays(nums, target):
    # Subset sum P with 2P = sum(nums) + target; count subsets (0/1 knapsack counting).
    total = sum(nums)
    s_plus_t = total + target
    if s_plus_t % 2 != 0:
        return 0
    p = s_plus_t // 2
    if p < 0 or p > total:
        return 0
    dp = [0] * (p + 1)
    dp[0] = 1
    for num in nums:
        for j in range(p, num - 1, -1):
            dp[j] += dp[j - num]
    return dp[p]


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 1, 1, 1, 1], 3, 5),
        # ([1], 1, 1),
        # ([1, 2, 3], 0, 2),
        # ([1], 0, 0),
        # ([0, 0, 0, 0, 0, 1], 1, 32),
        # ([100], -100, 1),
        # ([100], 100, 1),
        # ([1, 1], 0, 2),
        # ([1, 2, 7, 1, 5], 4, 2),
        # ([20,27,22,23,0,44,22,44,39,7,35,23,17,30,37,4,14,42,31,43], 38, 6008)
    ]

    print("=" * 70)
    print("LeetCode 494 - Target Sum")
    print("=" * 70)

    for nums, target, expected in test_cases:
        try:
            nums_copy = nums[:]
            result = findTargetSumWays(nums_copy, target)
            if result is None:
                print(f"⚠️  nums={nums}, target={target} -> Not implemented")
            else:
                is_correct = result == expected
                status = "✓" if is_correct else "✗"
                print(f"{status} nums={nums}, target={target}")
                print(f"   Output: {result}, Expected: {expected}")
        except Exception as e:
            print(f"❌ nums={nums}, target={target} -> Error: {e}")


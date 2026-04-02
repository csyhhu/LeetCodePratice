"""
[1027] Longest Arithmetic Subsequence
https://leetcode.com/problems/longest-arithmetic-subsequence/

Given an array nums of integers, return the length of the longest arithmetic
subsequence in nums.

Note that:
- A subsequence is a list that can be derived from nums by deleting some or
  no elements without changing the order of the remaining elements.
- A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value
  (for 0 <= i < seq.length - 1).

Example 1:
    Input: nums = [3,6,9,12]
    Output: 4
    Explanation: The whole array is an arithmetic sequence with steps of 3.

Example 2:
    Input: nums = [9,4,7,2,10]
    Output: 3
    Explanation: The longest arithmetic subsequence is [4,7,10].

Example 3:
    Input: nums = [20,1,15,3,10,5,8]
    Output: 4
    Explanation: The longest arithmetic subsequence is [20,15,10,5].

Constraints:
    - 2 <= nums.length <= 1000
    - 0 <= nums[i] <= 500

Date: 2026-03-31
"""

from typing import List


def longestArithSeqLength(nums: List[int]) -> int:
    # dp[i][eps] = max(dp[i-j][eps] for j in range(0, i) if nums[i] - nums[j] = eps)
    n = len(nums)
    # max_eps = 500 * 2 + 1
    # base = 500
    min_num = 500
    max_num = 0
    for num in nums:
        min_num = min(num, min_num)
        max_num = max(num, max_num)
    max_eps = max_num - min_num
    n_bucket = max_eps * 2 + 1
    # print(max_eps)
    dp = [[1] * (n_bucket) for _ in range(n)]
    for i in range(n):
        for j in range(0, i):
            eps = nums[i] - nums[j] + max_eps
            dp[i][eps] = max(dp[i][eps], dp[j][eps] + 1)

    max_len = 0
    # print(len(dp), len(dp[0]))
    # print(dp[n-1])
    # print(dp[n-1][-1])
    for i in range(n):
        for eps in range(n_bucket):
            # print(n-1, eps, dp[n-1][eps])
            max_len = max(max_len, dp[i][eps])
    # print(dp[n-1])
    return max_len


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([3, 6, 9, 12], 4),
        ([9, 4, 7, 2, 10], 3),
        ([20, 1, 15, 3, 10, 5, 8], 4),
    ]

    for nums, expected in test_cases:
        result = longestArithSeqLength(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} nums={nums}")
        print(f"   Output:   {result}")
        print(f"   Expected: {expected}\n")

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
    pass


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

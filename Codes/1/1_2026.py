"""
[1] Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return the indices of the two numbers
that add up to the target.

You may assume that each input has exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: nums[0] + nums[1] == 9, so we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

Constraints:
    - 2 <= nums.length <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= target <= 10^9
    - Only one valid answer exists.

Date: 2026-03-08
"""

def twoSum(nums, target):
    hashtable = {}
    for idx, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], idx]
        hashtable[num] = idx



# Test cases
if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([2, 1, 3], 4, [1, 2]),
        ([-1, -2, -3, 5, 10], 7, [3, 4]),
        ([1, 2, 3, 4, 5], 9, [3, 4]),
    ]
    
    print("=" * 70)
    print("LeetCode 1 - Two Sum")
    print("=" * 70)
    
    for nums, target, expected in test_cases:
        try:
            result = twoSum(nums, target)
            if result is None:
                print(f"⚠️  nums={nums}, target={target} -> Not implemented")
            else:
                is_correct = (set(result) == set(expected) and 
                             nums[result[0]] + nums[result[1]] == target)
                status = "✓" if is_correct else "✗"
                print(f"{status} nums={nums}, target={target} -> {result}")
        except Exception as e:
            print(f"❌ nums={nums}, target={target} -> Error: {e}")

"""
LeetCode 1004: Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/

Given a binary array nums and an integer k, return the maximum number of
consecutive 1's in the array if you can flip at most k 0's.

Example 1:
    Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    Output: 6
    Explanation: [1,1,1,0,0,1,1,1,1,1,1]
                              ^-----------^  (6 ones, flipped 2 zeros)

Example 2:
    Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
    Output: 10
    Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
                        ^-------------------^  (10 ones, flipped 3 zeros)

Constraints:
    - 1 <= nums.length <= 10^5
    - nums[i] is either 0 or 1.
    - 0 <= k <= nums.length
"""
from typing import List

"""
def longestOnes(nums: List[int], k: int) -> int:
    left, right = 0, 0
    n = len(nums)
    max_consecutive_1 = 0
    while True:
        # print(left, right, nums[left:right])
        if (right - left) - sum(nums[left:right]) <= k and right <= n - 1:
            right += 1
            max_consecutive_1 = max(max_consecutive_1, min(sum(nums[left:right]) + k, right - left))
        else:
            left += 1
        if left == right == n:
            break
    return max_consecutive_1
"""
def longestOnes(nums: List[int], k: int) -> int:
    left, right = 0, 0
    n = len(nums)
    max_consecutive_1 = 0
    n_zeros = 0
    while right < n:
        if nums[right] == 0:
            n_zeros += 1
        right += 1
        if n_zeros > k:
            if nums[left] == 0:
                n_zeros -= 1
            left += 1
        max_consecutive_1 = max(max_consecutive_1, right - left)
    return max_consecutive_1

# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "nums": [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],
            "k": 2,
            "expected": 6,
            "description": "Flip 2 zeros, max window = 6",
        },
        {
            "nums": [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
            "k": 3,
            "expected": 10,
            "description": "Flip 3 zeros, max window = 10",
        },
        {
            "nums": [1, 1, 1],
            "k": 0,
            "expected": 3,
            "description": "k=0, all ones already",
        },
        {
            "nums": [0, 0, 0],
            "k": 0,
            "expected": 0,
            "description": "k=0, all zeros",
        },
        {
            "nums": [0, 0, 0],
            "k": 3,
            "expected": 3,
            "description": "Flip all zeros",
        },
        {
            "nums": [1],
            "k": 0,
            "expected": 1,
            "description": "Single element 1",
        },
        {
            "nums": [0,0,1,1,1,0,0],
            "k": 0,
            "expected": 3,
            "description": "Flip 0 zeros, max window = 3",
        },
        {
            "nums": [0,0,0,1],
            "k": 4,
            "expected": 4,
            "description": "Flip 4 zeros, max window = 4",
        }
    ]

    print("=" * 65)
    print("LeetCode 1004: Max Consecutive Ones III - Test Results")
    print("=" * 65)

    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        result = longestOnes(test["nums"], test["k"])
        is_pass = result == test["expected"]
        status = "✅ PASS" if is_pass else "❌ FAIL"

        if is_pass:
            passed += 1
        else:
            failed += 1

        print(f"\nTest Case {i}: {status}")
        print(f"  Description: {test['description']}")
        print(f"  Input:       nums={test['nums']}, k={test['k']}")
        print(f"  Expected:    {test['expected']}")
        print(f"  Your Output: {result}")

    print("\n" + "=" * 65)
    print(f"Summary: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 65)

    if failed == 0:
        print("🎉 All test cases passed!")
    else:
        print(f"⚠️  {failed} test case(s) failed. Please review.")

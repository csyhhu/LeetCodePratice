"""
LeetCode 31: Next Permutation
https://leetcode.com/problems/next-permutation/

A permutation of an array of integers is an arrangement of its members into a
sequence or linear order.

The next permutation of an array of integers is the next lexicographically greater
permutation of its integer. More formally, if all the permutations of the array are
sorted in one container according to their lexicographical order, then the next
permutation of that array is the permutation that follows it in the sorted container.
If such arrangement is not possible, the array must be rearranged as the lowest
possible order (i.e., sorted in ascending order).

Modify nums in-place and do not return anything.

Example 1:
    Input: nums = [1,2,3]
    Output: [1,3,2]

Example 2:
    Input: nums = [3,2,1]
    Output: [1,2,3]

Example 3:
    Input: nums = [1,1,5]
    Output: [1,5,1]

Constraints:
    - 1 <= nums.length <= 100
    - 0 <= nums[i] <= 100
"""


def nextPermutation(nums: list[int]) -> None:
    n = len(nums)
    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            for j in range(n-1, i, -1):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    nums[i+1:] = reversed(nums[i+1:])
                    return
    nums[:] = nums[::-1]


# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "nums": [1, 2, 3],
            "expected": [1, 3, 2],
            "description": "Normal case",
        },
        {
            "nums": [3, 2, 1],
            "expected": [1, 2, 3],
            "description": "Descending order - wrap to lowest",
        },
        {
            "nums": [1, 1, 5],
            "expected": [1, 5, 1],
            "description": "With duplicates",
        },
        {
            "nums": [1],
            "expected": [1],
            "description": "Single element",
        },
        {
            "nums": [1, 3, 2],
            "expected": [2, 1, 3],
            "description": "Another normal case",
        },
        {
            "nums": [2, 3, 1],
            "expected": [3, 1, 2],
            "description": "Another normal case 2",
        },
    ]

    print("=" * 60)
    print("LeetCode 31: Next Permutation - Test Results")
    print("=" * 60)

    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        nums = test["nums"][:]
        nextPermutation(nums)
        result = nums
        is_pass = result == test["expected"]
        status = "✅ PASS" if is_pass else "❌ FAIL"

        if is_pass:
            passed += 1
        else:
            failed += 1

        print(f"\nTest Case {i}: {status}")
        print(f"  Description: {test['description']}")
        print(f"  Input:       nums={test['nums']}")
        print(f"  Expected:    {test['expected']}")
        print(f"  Your Output: {result}")

    print("\n" + "=" * 60)
    print(f"Summary: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 60)

    if failed == 0:
        print("🎉 All test cases passed!")
    else:
        print(f"⚠️  {failed} test case(s) failed. Please review.")

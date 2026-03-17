"""
[238] Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].

Requirements:
- Time complexity: O(n)
- Cannot use division
- Space complexity: O(1) (output array doesn't count)

Example:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

Date: 2026-02-28
"""

def productExceptSelf(nums):
    """
    思路：

    准备一个prefix[i]用于计算0->i的乘积（包含自身）。一个postfix[i]由于计算i->N-1的乘积（包含自身）。result[i] = prefix[i-1] * postfix[i+1]
    时间复杂度：O(n)
    空间复杂度：O(1) (不算输出数组)
    """
    n = len(nums)
    prefix = [1] * (n + 1)
    postfix = [1] * (n + 1)
    result = [1] * len(nums)
    for idx in range(1, n + 1):
        prefix[idx] = prefix[idx-1] * nums[idx-1]
    for idx in range(n-1, -1, -1):
        postfix[idx] = postfix[idx+1] * nums[idx]
    for idx in range(n):
        result[idx] = prefix[idx] * postfix[idx+1]
    # print(prefix)
    # print(postfix)
    return result


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3, 4]
    expected1 = [24, 12, 8, 6]
    result1 = productExceptSelf(nums1)
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print(f"Expected: {expected1}")
    print(f"Pass: {result1 == expected1}\n")

    # Test case 2
    nums2 = [-1, 1, 0, -3, 3]
    expected2 = [0, 0, 9, 0, 0]
    result2 = productExceptSelf(nums2)
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
    print(f"Expected: {expected2}")
    print(f"Pass: {result2 == expected2}\n")

"""
LeetCode 264: Ugly Number II
https://leetcode.com/problems/ugly-number-ii/

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

Example 1:
    Input: n = 10
    Output: 12
    Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:
    Input: n = 1
    Output: 1
    Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Constraints:
    - 1 <= n <= 1690

Hints:
    - The ugly number sequence is: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, ...
    - Each ugly number must be 2x, 3x, or 5x of a previous ugly number.
    - Use three pointers p2, p3, p5 pointing into the dp array.
    - dp[i] = min(dp[p2]*2, dp[p3]*3, dp[p5]*5), then advance the pointer(s) that produced the min.
    - Be careful to advance ALL pointers that equal the current min (avoid duplicates).
"""
from typing import List


def nthUglyNumber(n: int) -> int:
    # dp[i] = min(dp[p2]*2, dp[p3]*3, dp[p5]*5)
    # p2 from i-1 to 0, until dp[p2]*2 in dp
    dp = [1] * n
    p2 = p3 = p5 = 0
    for i in range(1, n):
        while dp[p2] * 2 <= dp[i-1] and p2 < n:
            p2 += 1
        while dp[p3] * 3 <= dp[i-1] and p3 < n:
            p3 += 1
        while dp[p5] * 5 <= dp[i-1] and p5 < n:
            p5 += 1
        dp[i] = min(dp[p2]*2, dp[p3]*3, dp[p5]*5)
    # print(dp)
    return dp[n-1]


# Test cases
if __name__ == "__main__":
    test_cases = [
        {"n": 1,    "expected": 1,    "description": "1st ugly number is 1"},
        {"n": 2,    "expected": 2,    "description": "2nd ugly number is 2"},
        {"n": 7,    "expected": 8,    "description": "7th ugly number is 8"},
        {"n": 10,   "expected": 12,   "description": "10th ugly number is 12"},
        {"n": 11,   "expected": 15,   "description": "11th ugly number is 15"},
        {"n": 15,   "expected": 24,   "description": "15th ugly number is 24"},
        {"n": 1690, "expected": 2123366400, "description": "Max n=1690"},
    ]

    print("=" * 65)
    print("LeetCode 264: Ugly Number II - Test Results")
    print("=" * 65)

    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        result = nthUglyNumber(test["n"])
        is_pass = result == test["expected"]
        status = "✅ PASS" if is_pass else "❌ FAIL"

        if is_pass:
            passed += 1
        else:
            failed += 1

        print(f"\nTest Case {i}: {status}")
        print(f"  Description: {test['description']}")
        print(f"  Input:       n={test['n']}")
        print(f"  Expected:    {test['expected']}")
        print(f"  Your Output: {result}")

    print("\n" + "=" * 65)
    print(f"Summary: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 65)

    if failed == 0:
        print("🎉 All test cases passed!")
    else:
        print(f"⚠️  {failed} test case(s) failed. Please review.")

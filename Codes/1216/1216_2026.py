"""
LeetCode 1216: Valid Palindrome III
https://leetcode.com/problems/valid-palindrome-iii/

Given a string s and an integer k, return true if s is a k-palindrome.

A string is k-palindrome if it can be transformed into a palindrome by
removing at most k characters from it.

Example 1:
    Input: s = "abcdeca", k = 2
    Output: true
    Explanation: Remove 'b' and 'e' characters.

Example 2:
    Input: s = "abbababa", k = 1
    Output: true

Constraints:
    - 1 <= s.length <= 1000
    - s consists of lowercase English letters.
    - 1 <= k <= s.length

Hint:
    - LeetCode 680 allowed deleting at most 1 character. This is the generalized version.
    - Think about what "minimum deletions to make a palindrome" means.
    - This is equivalent to: len(s) - LPS(s), where LPS is the Longest Palindromic Subsequence.
    - Or equivalently: the minimum number of deletions = len(s) - LCS(s, reverse(s)).
"""


def isValidPalindrome(s: str, k: int) -> bool:
    # dp[i][j] = dp[i+1][j-1] + 2 or max(dp[i+1][j], dp[i][j-1])
    n = len(s)
    dp = [[0] * (n) for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1): # lenth = n + 1, i = 0, j = n
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    # print(dp[0][n-1])
    return n - dp[0][n-1] <= k


# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "s": "abcdeca",
            "k": 2,
            "expected": True,
            "description": "Remove 'b' and 'e'",
        },
        {
            "s": "abbababa",
            "k": 1,
            "expected": True,
            "description": "Remove 1 char to form palindrome",
        },
        {
            "s": "abc",
            "k": 1,
            "expected": False,
            "description": "Need to remove 2 chars, but k=1",
        },
        {
            "s": "abca",
            "k": 1,
            "expected": True,
            "description": "Same as LeetCode 680 case",
        },
        {
            "s": "abcba",
            "k": 0,
            "expected": True,
            "description": "Already a palindrome, k=0",
        },
        {
            "s": "abcdba",
            "k": 2,
            "expected": True,
            "description": "Remove 'c' and 'd' to get 'abba'",
        },
        {
            "s": "fcvmzuecmfgv",
            "k": 3,
            "expected": False,
            "description": "Not achievable with k=3",
        },
    ]

    print("=" * 60)
    print("LeetCode 1216: Valid Palindrome III - Test Results")
    print("=" * 60)

    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        result = isValidPalindrome(test["s"], test["k"])
        is_pass = result == test["expected"]
        status = "✅ PASS" if is_pass else "❌ FAIL"

        if is_pass:
            passed += 1
        else:
            failed += 1

        print(f"\nTest Case {i}: {status}")
        print(f"  Description: {test['description']}")
        print(f"  Input:       s=\"{test['s']}\", k={test['k']}")
        print(f"  Expected:    {test['expected']}")
        print(f"  Your Output: {result}")

    print("\n" + "=" * 60)
    print(f"Summary: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 60)

    if failed == 0:
        print("🎉 All test cases passed!")
    else:
        print(f"⚠️  {failed} test case(s) failed. Please review.")

"""
LeetCode 44: Wildcard Matching
https://leetcode.com/problems/wildcard-matching/

Given an input string s and a pattern p, implement wildcard pattern matching
with support for '?' and '*' where:
    - '?' matches any single character.
    - '*' matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Example 1:
    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".

Example 2:
    Input: s = "aa", p = "*"
    Output: true
    Explanation: '*' matches any sequence.

Example 3:
    Input: s = "cb", p = "?a"
    Output: false
    Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
    Input: s = "adceb", p = "*a*b"
    Output: true
    Explanation: '*' matches the empty sequence, "a" matches "a", '*' matches "dce", "b" matches "b".

Example 5:
    Input: s = "acdcb", p = "a*c?b"
    Output: false

Constraints:
    - 0 <= s.length, p.length <= 2000
    - s contains only lowercase English letters.
    - p contains only lowercase English letters, '?' or '*'.
"""


def isMatch(s: str, p: str) -> bool:
    # from p to s
    # dp[i][j] = dp[i-1]][j-1] if p[i] = s[j] or p[i] = '?'
    # dp[i][j] = dp[i][j-1] if p[i] = '*'
    n = len(p)
    m = len(s)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True
    # Deal with the case that p starts with *
    for i in range(1, n + 1):
        if p[i-1] == '*':
            dp[i][0] = dp[i-1][0]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[i-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            else:
                dp[i][j] = (p[i-1] == '?' or p[i-1] == s[j-1]) and dp[i-1][j-1]

    return dp[n][m]


# Test cases
if __name__ == "__main__":
    test_cases = [
        {"s": "aa", "p": "a", "expected": False, "description": "Pattern shorter than string"},
        {"s": "aa", "p": "*", "expected": True, "description": "Star matches everything"},
        {"s": "cb", "p": "?a", "expected": False, "description": "? matches c but a != b"},
        {"s": "adceb", "p": "*a*b", "expected": True, "description": "Stars match substrings"},
        {"s": "acdcb", "p": "a*c?b", "expected": False, "description": "Pattern mismatch"},
        {"s": "", "p": "", "expected": True, "description": "Both empty"},
        {"s": "", "p": "*", "expected": True, "description": "Empty string, star pattern"},
        {"s": "abc", "p": "a?c", "expected": True, "description": "? matches b"},
        {"s": "abc", "p": "a**c", "expected": True, "description": "Multiple stars"},
    ]

    print("=" * 60)
    print("LeetCode 44: Wildcard Matching - Test Results")
    print("=" * 60)

    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        result = isMatch(test["s"], test["p"])
        is_pass = result == test["expected"]
        status = "✅ PASS" if is_pass else "❌ FAIL"

        if is_pass:
            passed += 1
        else:
            failed += 1

        print(f"\nTest Case {i}: {status}")
        print(f"  Description: {test['description']}")
        print(f"  Input:       s=\"{test['s']}\", p=\"{test['p']}\"")
        print(f"  Expected:    {test['expected']}")
        print(f"  Your Output: {result}")

    print("\n" + "=" * 60)
    print(f"Summary: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 60)

    if failed == 0:
        print("🎉 All test cases passed!")
    else:
        print(f"⚠️  {failed} test case(s) failed. Please review.")

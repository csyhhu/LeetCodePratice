"""
LeetCode 1143: Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/

Given two strings text1 and text2, return the length of their longest common
subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string
with some characters (can be none) deleted without changing the relative order
of the remaining characters.

A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
    Input: text1 = "abcde", text2 = "ace"
    Output: 3
    Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
    Input: text1 = "abc", text2 = "abc"
    Output: 3
    Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
    Input: text1 = "abc", text2 = "def"
    Output: 0
    Explanation: There is no such common subsequence, so the result is 0.

Constraints:
    - 1 <= text1.length, text2.length <= 1000
    - text1 and text2 consist of only lowercase English characters.

与 LeetCode 115 对比：
    - 115：s 中有多少个子序列等于 t（方案数，单向匹配）
    - 1143：两个字符串的最长公共子序列长度（最优化，双向对称）
    - 同样是二维 DP，dp[i][j] 的转移方向很相似

Hint:
    定义 dp[i][j] = text1[:i] 和 text2[:j] 的最长公共子序列长度
    思考：当 text1[i-1] == text2[j-1] 时，dp[i][j] 是多少？
          当 text1[i-1] != text2[j-1] 时，dp[i][j] 是多少？
"""


def longestCommonSubsequence(text1: str, text2: str) -> int:
    # dp[i][j] = dp[i-1][j-1] + 1 if text1[i-1] == text2[j-1]  max(else dp[i-1][j], dp[i][j-1])
    n1 = len(text1)
    n2 = len(text2)
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n1][n2]


# Test cases
if __name__ == "__main__":
    test_cases = [
        {"text1": "abcde", "text2": "ace", "expected": 3, "description": "LCS is 'ace'"},
        {"text1": "abc", "text2": "abc", "expected": 3, "description": "Identical strings"},
        {"text1": "abc", "text2": "def", "expected": 0, "description": "No common subsequence"},
        {"text1": "bl", "text2": "yby", "expected": 1, "description": "LCS is 'b'"},
        {"text1": "abcba", "text2": "abcbcba", "expected": 5, "description": "LCS is 'abcba'"},
        {"text1": "a", "text2": "a", "expected": 1, "description": "Single char match"},
        {"text1": "a", "text2": "b", "expected": 0, "description": "Single char no match"},
        {"text1": "ezupkr", "text2": "ubmrapg", "expected": 2, "description": "LCS is 'ur'"},
    ]

    print("=" * 60)
    print("LeetCode 1143: Longest Common Subsequence - Test Results")
    print("=" * 60)

    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        result = longestCommonSubsequence(test["text1"], test["text2"])
        is_pass = result == test["expected"]
        status = "✅ PASS" if is_pass else "❌ FAIL"

        if is_pass:
            passed += 1
        else:
            failed += 1

        print(f"\nTest Case {i}: {status}")
        print(f"  Description: {test['description']}")
        print(f"  Input:       text1=\"{test['text1']}\", text2=\"{test['text2']}\"")
        print(f"  Expected:    {test['expected']}")
        print(f"  Your Output: {result}")

    print("\n" + "=" * 60)
    print(f"Summary: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 60)

    if failed == 0:
        print("🎉 All test cases passed!")
    else:
        print(f"⚠️  {failed} test case(s) failed. Please review.")

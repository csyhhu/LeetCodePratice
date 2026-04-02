"""
LeetCode 516: Longest Palindromic Subsequence
https://leetcode.com/problems/longest-palindromic-subsequence/

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by
deleting some or no elements without changing the order of the remaining elements.

Example 1:
    Input: s = "bbbab"
    Output: 4
    Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
    Input: s = "cbbd"
    Output: 2
    Explanation: One possible longest palindromic subsequence is "bb".

Constraints:
    - 1 <= s.length <= 1000
    - s consists only of lowercase English letters.

与前面的字符串 DP 对比：
    - 115 / 1143 / 72：二维 dp，两个字符串，i 和 j 分别扫描两个字符串
    - 516：区间 DP，只有一个字符串，dp[i][j] 表示 s[i..j] 范围内的答案
    - 区间 DP 的特点：需要先算小区间，再扩展到大区间（枚举顺序很重要！）

Hint:
    定义 dp[i][j] = s[i..j]（含两端）的最长回文子序列长度
    边界条件：
        dp[i][i] = 1  (单个字符本身就是长度为 1 的回文)
    转移：
        当 s[i] == s[j] 时，两端字符可以同时加入，dp[i][j] = ?
        当 s[i] != s[j] 时，只能舍弃其中一端，dp[i][j] = ?
    枚举顺序：
        外层枚举区间长度 length（从 2 到 n），内层枚举左端点 i
        注意 j = i + length - 1

    进阶思路（选做）：
        能否转化为 1143 的问题？s 和 reverse(s) 的 LCS 是什么？
"""


def longestPalindromeSubseq(s: str) -> int:
    # dp[i][j]: from i to j, the length of longtest palindrome subsequence
    # if s[i] == s[j]: dp[i][j] = dp[i+1][j-1] + 2
    # else: dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n):
        for i in range(1, n + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[n-1][n-1]


# Test cases
if __name__ == "__main__":
    test_cases = [
        {"s": "bbbab", "expected": 4, "description": "LPS is 'bbbb'"},
        {"s": "cbbd", "expected": 2, "description": "LPS is 'bb'"},
        {"s": "a", "expected": 1, "description": "Single character"},
        {"s": "aa", "expected": 2, "description": "Two same chars"},
        {"s": "ab", "expected": 1, "description": "Two different chars"},
        {"s": "abcba", "expected": 5, "description": "Entire string is palindrome"},
        {"s": "abcd", "expected": 1, "description": "All different, LPS length 1"},
        {"s": "agbdba", "expected": 5, "description": "LPS is 'abdba'"},
        {"s": "aabaa", "expected": 5, "description": "LPS is 'aabaa'"},
        {"s": "leetcode", "expected": 4, "description": "LPS is 'eeee' or similar"},
    ]

    print("=" * 60)
    print("LeetCode 516: Longest Palindromic Subsequence - Test Results")
    print("=" * 60)

    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        result = longestPalindromeSubseq(test["s"])
        is_pass = result == test["expected"]
        status = "✅ PASS" if is_pass else "❌ FAIL"

        if is_pass:
            passed += 1
        else:
            failed += 1

        print(f"\nTest Case {i}: {status}")
        print(f"  Description: {test['description']}")
        print(f"  Input:       s=\"{test['s']}\"")
        print(f"  Expected:    {test['expected']}")
        print(f"  Your Output: {result}")

    print("\n" + "=" * 60)
    print(f"Summary: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 60)

    if failed == 0:
        print("🎉 All test cases passed!")
    else:
        print(f"⚠️  {failed} test case(s) failed. Please review.")

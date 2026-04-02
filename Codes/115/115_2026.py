"""
LeetCode 115: Distinct Subsequences
https://leetcode.com/problems/distinct-subsequences/

Given two strings s and t, return the number of distinct subsequences of s
which equals t.

A subsequence of a string is a new string formed from the original string
by deleting some (can be zero) characters without disturbing the remaining
characters' relative positions.

Example 1:
    Input: s = "rabbbit", t = "rabbit"
    Output: 3
    Explanation: There are 3 ways to get "rabbit" from "rabbbit":
        rabb[b]it -> rabbit (delete the 3rd 'b')
        rab[b]bit -> rabbit (delete the 2nd 'b')
        ra[b]bbit -> rabbit (delete the 1st 'b')

Example 2:
    Input: s = "babgbag", t = "bag"
    Output: 5
    Explanation: There are 5 ways to get "bag" from "babgbag":
        [b]a[b]g[bag] ...

Constraints:
    - 1 <= s.length, t.length <= 1000
    - s and t consist of English letters.

与 LeetCode 10 / 44 对比：
    - 10 / 44：是否能匹配（返回 bool）
    - 115：有多少种匹配方式（返回 int）
    - 同样是二维 DP，dp[i][j] 含义要仔细定义

Hint:
    定义 dp[i][j] = 用 s[:i] 构成 t[:j] 的方案数
    思考：当 s[i-1] == t[j-1] 时，有哪两种选择？
          当 s[i-1] != t[j-1] 时，只能怎么做？
"""


def numDistinct(s: str, t: str) -> int:
    # if s[i-1] == t[j-1]
    #   # Take or not take the character
    #   dp[i][j] = dp[i-1][j-1] + dp[i-2][j-1]
    # if s[i-1] != t[j-1]
    #   dp[i][j] = dp[i-1][j-1]
    # dp[0][0] = True
    # dp[i][0] = True
    n = len(s)
    m = len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    # print(dp)
    return dp[n][m]


# Test cases
if __name__ == "__main__":
    test_cases = [
        {"s": "rabbbit", "t": "rabbit", "expected": 3, "description": "3 ways to pick rabbit from rabbbit"},
        {"s": "babgbag", "t": "bag", "expected": 5, "description": "5 ways to pick bag from babgbag"},
        {"s": "a", "t": "a", "expected": 1, "description": "Single char match"},
        {"s": "aa", "t": "a", "expected": 2, "description": "Two choices for single char"},
        {"s": "abc", "t": "abc", "expected": 1, "description": "Exact match, only one way"},
        {"s": "abc", "t": "d", "expected": 0, "description": "No match at all"},
        {"s": "aaa", "t": "aa", "expected": 3, "description": "C(3,2)=3 ways to pick 2 a's"},
        {"s": "b", "t": "b", "expected": 1, "description": "Simple single match"},
    ]

    print("=" * 60)
    print("LeetCode 115: Distinct Subsequences - Test Results")
    print("=" * 60)

    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        result = numDistinct(test["s"], test["t"])
        is_pass = result == test["expected"]
        status = "✅ PASS" if is_pass else "❌ FAIL"

        if is_pass:
            passed += 1
        else:
            failed += 1

        print(f"\nTest Case {i}: {status}")
        print(f"  Description: {test['description']}")
        print(f"  Input:       s=\"{test['s']}\", t=\"{test['t']}\"")
        print(f"  Expected:    {test['expected']}")
        print(f"  Your Output: {result}")

    print("\n" + "=" * 60)
    print(f"Summary: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 60)

    if failed == 0:
        print("🎉 All test cases passed!")
    else:
        print(f"⚠️  {failed} test case(s) failed. Please review.")

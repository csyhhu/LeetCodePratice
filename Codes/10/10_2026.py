"""
LeetCode 10: Regular Expression Matching
https://leetcode.com/problems/regular-expression-matching/

Given an input string s and a pattern p, implement regular expression matching
with support for '.' and '*' where:
    - '.' matches any single character.
    - '*' matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Example 1:
    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".

Example 2:
    Input: s = "aa", p = "a*"
    Output: true
    Explanation: '*' means zero or more of the preceding element, 'a'.
                 Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
    Input: s = "ab", p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
    Input: s = "aab", p = "c*a*b"
    Output: true
    Explanation: 'c' can be repeated 0 times, 'a' can be repeated 2 times.
                 So the pattern matches "aab".

Example 5:
    Input: s = "mississippi", p = "mis*is*p*."
    Output: false

Constraints:
    - 1 <= s.length <= 20
    - 1 <= p.length <= 30
    - s contains only lowercase English letters.
    - p contains only lowercase English letters and '.', '*'.
    - It is guaranteed for each occurrence of '*', there will be a previous valid character to match.

Hint:
    与 LeetCode 44 (Wildcard Matching) 对比：
    - 44 题：'*' 是独立通配符，可匹配任意序列
    - 10 题：'*' 必须跟在某个字符后，表示"前一字符出现 0 次或多次"

    DP 定义：dp[i][j] = s[:i] 能否被 p[:j] 匹配

    思考：当 p[j-1] == '*' 时，应该怎么处理？
          注意 '*' 不能单独出现，它一定是 "x*" 这样的组合（x 是前一个字符）
"""


def isMatch(s: str, p: str) -> bool:
    # p[i] <=> s[j]
    # if p[i] = '*'
    #   if '*' acts as erase:
    #       dp[i][j] = dp[i-2][j] or i <= 1
    #   if '*' acts as match:
    #       dp[i][j] = dp[i-1][j-1] and p[i] = s[j]
    n = len(p)
    m = len(s)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(2, n+1):
        if p[i-1] == '*':
            dp[i][0] = dp[i-2][0]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[i-1] == '.':
                dp[i][j] = dp[i-1][j-1]
            elif p[i-1] == '*': # 'c*' -> '': dp[2][0] = dp[0][0] = True
                dp[i][j] = dp[i-2][j] or (dp[i][j-1] and (p[i-2] == s[j-1] or p[i-2] == '.'))
            else:
                dp[i][j] = dp[i-1][j-1] and p[i-1] == s[j-1]
    # print(dp)
    return dp[n][m]


# Test cases
if __name__ == "__main__":
    test_cases = [
        {"s": "aa", "p": "a", "expected": False, "description": "Pattern shorter than string"},
        {"s": "aa", "p": "a*", "expected": True, "description": "'a*' matches 'aa'"},
        {"s": "ab", "p": ".*", "expected": True, "description": "'.*' matches any string"},
        {"s": "aab", "p": "c*a*b", "expected": True, "description": "c* = empty, a* = aa"},
        {"s": "mississippi", "p": "mis*is*p*.", "expected": False, "description": "Classic tricky case"},
        {"s": "", "p": "", "expected": True, "description": "Both empty"},
        {"s": "", "p": "a*", "expected": True, "description": "Empty string, a* = zero a's"},
        {"s": "", "p": "a*b*c*", "expected": True, "description": "Empty string, all zero repetitions"},
        {"s": "a", "p": "ab*", "expected": True, "description": "b* matches zero b's"},
        {"s": "aaa", "p": "a*a", "expected": True, "description": "a* consumes first two a's"},
        {"s": "aaa", "p": "ab*a", "expected": False, "description": "b* is zero, but need two a's at end"},
        {"s": "aaa", "p": "a*", "expected": True, "description": "a* matches all"},
    ]

    print("=" * 60)
    print("LeetCode 10: Regular Expression Matching - Test Results")
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

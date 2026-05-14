"""
LeetCode 97: Interleaving String
https://leetcode.com/problems/interleaving-string/

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving
of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are
divided into n and m substrings respectively, such that:
    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + ...

Example 1:
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    Output: true

Example 2:
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
    Output: false

Example 3:
    Input: s1 = "", s2 = "", s3 = ""
    Output: true

Constraints:
    - 0 <= s1.length, s2.length <= 100
    - 0 <= s3.length <= 200
    - s1, s2, s3 consist of lowercase English letters.
"""


def isInterleave(s1: str, s2: str, s3: str) -> bool:
    # dp[i][j]: Fessibility when getting length i from s1 and length j from s2, leading to length i+j in s3
    # dp[i][j] = dp[i][j-1] if s3[i+j-1] == s2[j-1] or dp[i-1][j] if s3[i+j-1] == s1[i-1]
    n1, n2, n3 = len(s1), len(s2), len(s3)
    dp = [[False for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    if n1 == 0:
        return s3 == s2
    elif n2 == 0:
        return s3 == s1
    elif n1 == 0 and n2 == 0:
        return s3 == s1
    if n1 + n2 != n3:
        return False

    # dp[0][0] = True
    # dp[1][0] = True if s1[0] == s3[0] else False
    # dp[0][1] = True if s2[0] == s3[0] else False
    for i in range(1, n1+1):
        if s3[i-1] == s1[i-1]:
            dp[i][0] = True
        else:
            break
    for j in range(1, n2+1):
        if s3[j-1] == s2[j-1]:
            dp[0][j] = True
        else:
            break
    # print(dp)
    # """
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            print(i+j-1, i-1, j-1)
            if (s3[i+j-1] == s2[j-1]) or (s3[i+j-1] == s1[i-1]):
                dp[i][j] = dp[i][j-1] or dp[i-1][j]
            if s3[i+j-1] == s2[j-1]:
                dp[i][j] = dp[i][j-1]
            elif s3[i+j-1] == s1[i-1]:
                dp[i][j] = dp[i-1][j]
    # """
    """
    for length in range(1, n3 + 1):
        for i in range(1, n1 + 1):
            j = length - i
            if j <= 0 or j > n2:
                continue
            print(length - 1, i-1, j-1)
            if (s3[length - 1] == s2[j-1]) and (s3[length - 1] == s1[i-1]):
                dp[i][j] = dp[i][j-1] or dp[i-1][j]
            elif s3[length - 1] == s2[j-1]:
                dp[i][j] = dp[i][j-1]
            elif s3[length - 1] == s1[i-1]:
                dp[i][j] = dp[i-1][j]
    """
    # print(dp)
    return dp[n1][n2]


# Test cases
if __name__ == "__main__":
    test_cases = [
        # {
        #     "s1": "aabcc",
        #     "s2": "dbbca",
        #     "s3": "aadbbcbcac",
        #     "expected": True,
        #     "description": "Standard interleaving",
        # },
        # {
        #     "s1": "aabcc",
        #     "s2": "dbbca",
        #     "s3": "aadbbbaccc",
        #     "expected": False,
        #     "description": "Not a valid interleaving",
        # },
        # {
        #     "s1": "",
        #     "s2": "",
        #     "s3": "",
        #     "expected": True,
        #     "description": "All empty strings",
        # },
        # {
        #     "s1": "a",
        #     "s2": "b",
        #     "s3": "ab",
        #     "expected": True,
        #     "description": "Simple case s1+s2",
        # },
        # {
        #     "s1": "a",
        #     "s2": "b",
        #     "s3": "ba",
        #     "expected": True,
        #     "description": "Simple case s2+s1",
        # },
        # {
        #     "s1": "a",
        #     "s2": "b",
        #     "s3": "abc",
        #     "expected": False,
        #     "description": "Length mismatch",
        # },
        # {
        #     "s1": "ab",
        #     "s2": "bc",
        #     "s3": "bbac",
        #     "expected": False,
        #     "description": "Tricky overlapping characters",
        # },
        {
            "s1": "db",
            "s2": "b",
            "s3": "cbb",
            "expected": False,
            "description": "Test case from LC",
        }
    ]

    print("=" * 60)
    print("LeetCode 97: Interleaving String - Test Results")
    print("=" * 60)

    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        result = isInterleave(test["s1"], test["s2"], test["s3"])
        is_pass = result == test["expected"]
        status = "✅ PASS" if is_pass else "❌ FAIL"

        if is_pass:
            passed += 1
        else:
            failed += 1

        print(f"\nTest Case {i}: {status}")
        print(f"  Description: {test['description']}")
        print(f"  Input:       s1=\"{test['s1']}\", s2=\"{test['s2']}\", s3=\"{test['s3']}\"")
        print(f"  Expected:    {test['expected']}")
        print(f"  Your Output: {result}")

    print("\n" + "=" * 60)
    print(f"Summary: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 60)

    if failed == 0:
        print("🎉 All test cases passed!")
    else:
        print(f"⚠️  {failed} test case(s) failed. Please review.")

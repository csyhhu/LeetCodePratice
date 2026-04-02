"""
LeetCode 62: Unique Paths
https://leetcode.com/problems/unique-paths/

There is a robot on an m x n grid. The robot is initially located at the
top-left corner (i.e., grid[0][0]). The robot tries to move to the
bottom-right corner (i.e., grid[m-1][n-1]).

The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths
that the robot can take to reach the bottom-right corner.

Example 1:
    Input: m = 3, n = 7
    Output: 28

Example 2:
    Input: m = 3, n = 2
    Output: 3
    Explanation: From the top-left corner, there are a total of 3 ways to
                 reach the bottom-right corner:
                 1. Right -> Down -> Down
                 2. Down -> Down -> Right
                 3. Down -> Right -> Down

Constraints:
    - 1 <= m, n <= 100
"""


def uniquePaths(m: int, n: int) -> int:
    # dp[i][j] = dp[i-1][j] + dp[i][j-1]
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]


# Test cases
if __name__ == "__main__":
    test_cases = [
        {"m": 3, "n": 7, "expected": 28, "description": "3x7 grid"},
        {"m": 3, "n": 2, "expected": 3, "description": "3x2 grid"},
        {"m": 1, "n": 1, "expected": 1, "description": "1x1 grid, already at destination"},
        {"m": 2, "n": 2, "expected": 2, "description": "2x2 grid"},
        {"m": 1, "n": 100, "expected": 1, "description": "1-row grid, only one path"},
        {"m": 100, "n": 1, "expected": 1, "description": "1-col grid, only one path"},
    ]

    print("=" * 55)
    print("LeetCode 62: Unique Paths - Test Results")
    print("=" * 55)

    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        result = uniquePaths(test["m"], test["n"])
        is_pass = result == test["expected"]
        status = "✅ PASS" if is_pass else "❌ FAIL"

        if is_pass:
            passed += 1
        else:
            failed += 1

        print(f"\nTest Case {i}: {status}")
        print(f"  Description: {test['description']}")
        print(f"  Input:       m={test['m']}, n={test['n']}")
        print(f"  Expected:    {test['expected']}")
        print(f"  Your Output: {result}")

    print("\n" + "=" * 55)
    print(f"Summary: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 55)

    if failed == 0:
        print("🎉 All test cases passed!")
    else:
        print(f"⚠️  {failed} test case(s) failed. Please review.")

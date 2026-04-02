"""
LeetCode 64: Minimum Path Sum
https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
    Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
    Output: 7
    Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
    Input: grid = [[1,2,3],[4,5,6]]
    Output: 12

Constraints:
    - m == grid.length
    - n == grid[i].length
    - 1 <= m, n <= 200
    - 0 <= grid[i][j] <= 200
"""


def minPathSum(grid: list[list[int]]) -> int:
    # dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    dp = [[0] * len(grid[0]) for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j-1] + grid[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[-1][-1]


# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "grid": [[1, 3, 1], [1, 5, 1], [4, 2, 1]],
            "expected": 7,
            "description": "3x3 grid, path: 1→3→1→1→1",
        },
        {
            "grid": [[1, 2, 3], [4, 5, 6]],
            "expected": 12,
            "description": "2x3 grid",
        },
        {
            "grid": [[1]],
            "expected": 1,
            "description": "1x1 grid",
        },
        {
            "grid": [[1, 2], [1, 1]],
            "expected": 3,
            "description": "2x2 grid",
        },
        {
            "grid": [[0, 0, 0], [0, 0, 0]],
            "expected": 0,
            "description": "all zeros grid",
        },
    ]

    print("=" * 55)
    print("LeetCode 64: Minimum Path Sum - Test Results")
    print("=" * 55)

    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        result = minPathSum(test["grid"])
        is_pass = result == test["expected"]
        status = "✅ PASS" if is_pass else "❌ FAIL"

        if is_pass:
            passed += 1
        else:
            failed += 1

        print(f"\nTest Case {i}: {status}")
        print(f"  Description: {test['description']}")
        print(f"  Input:       grid={test['grid']}")
        print(f"  Expected:    {test['expected']}")
        print(f"  Your Output: {result}")

    print("\n" + "=" * 55)
    print(f"Summary: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 55)

    if failed == 0:
        print("🎉 All test cases passed!")
    else:
        print(f"⚠️  {failed} test case(s) failed. Please review.")

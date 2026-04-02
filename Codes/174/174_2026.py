"""
LeetCode 174: Dungeon Game
https://leetcode.com/problems/dungeon-game/

The demons had captured the princess and imprisoned her in the bottom-right corner of
a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Heroic knight
was hired to rescue the princess.

The knight's initial health point is a positive integer. If at any point his health
point drops to 0 or below, he dies immediately.

Some rooms contain demons (represented by negative integers), so the knight loses
health upon entering these rooms; other rooms are either empty (0) or contain magic
orbs that increase the knight's health (positive integers).

The knight has been initially positioned at the top-left room and must fight his way
through dungeon to rescue the princess.

The knight can only move either right or down at each step.

Return the knight's minimum initial health so that he can rescue the princess.

Note that the knight's health has no upper bound.

Example 1:
    Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
    Output: 7
    Explanation: The initial health of the knight must be at least 7 if he follows
                 the optimal path: RIGHT -> RIGHT -> DOWN -> DOWN.

Example 2:
    Input: dungeon = [[0]]
    Output: 1

Constraints:
    - m == dungeon.length
    - n == dungeon[i].length
    - 1 <= m, n <= 200
    - -1000 <= dungeon[i][j] <= 1000

Hint: Think about this in reverse - what is the minimum health required when LEAVING
     each room, and work backwards from the bottom-right corner.
"""


def calculateMinimumHP(dungeon: list[list[int]]) -> int:
    # dp[i] = dp[i-1][j] - dungeon[i][j]
    m, n = len(dungeon), len(dungeon[0])
    dp = [[0] * n for _ in range(m)]
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i == m-1 and j == n-1:
                dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
            elif i == m-1:
                dp[i][j] = max(1, dp[i][j+1] - dungeon[i][j])
            elif j == n-1:
                dp[i][j] = max(1, dp[i+1][j] - dungeon[i][j])
            else:
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
    return dp[0][0]


# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "dungeon": [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]],
            "expected": 7,
            "description": "3x3 dungeon, optimal path: RIGHT->RIGHT->DOWN->DOWN",
        },
        {
            "dungeon": [[0]],
            "expected": 1,
            "description": "1x1 dungeon with 0 room",
        },
        {
            "dungeon": [[1]],
            "expected": 1,
            "description": "1x1 dungeon with positive room",
        },
        {
            "dungeon": [[-5]],
            "expected": 6,
            "description": "1x1 dungeon with negative room, must start with at least 6",
        },
        {
            "dungeon": [[1, -3, 3], [0, -2, 0], [-3, -3, -3]],
            "expected": 3,
            "description": "3x3 dungeon",
        },
    ]

    print("=" * 60)
    print("LeetCode 174: Dungeon Game - Test Results")
    print("=" * 60)

    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        result = calculateMinimumHP(test["dungeon"])
        is_pass = result == test["expected"]
        status = "✅ PASS" if is_pass else "❌ FAIL"

        if is_pass:
            passed += 1
        else:
            failed += 1

        print(f"\nTest Case {i}: {status}")
        print(f"  Description: {test['description']}")
        print(f"  Input:       dungeon={test['dungeon']}")
        print(f"  Expected:    {test['expected']}")
        print(f"  Your Output: {result}")

    print("\n" + "=" * 60)
    print(f"Summary: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 60)

    if failed == 0:
        print("🎉 All test cases passed!")
    else:
        print(f"⚠️  {failed} test case(s) failed. Please review.")

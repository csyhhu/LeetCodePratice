"""
[994] Rotting Oranges
https://leetcode.com/problems/rotting-oranges/

You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is
impossible, return -1.

Example 1:
    Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4

Example 2:
    Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting
    only happens 4-directionally.

Example 3:
    Input: grid = [[0,2]]
    Output: 0
    Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:
    - m == grid.length
    - n == grid[i].length
    - 1 <= m, n <= 10
    - grid[i][j] is 0, 1, or 2.
"""


def orangesRotting(grid):

    def rot(grid):
        n_row, n_col = len(grid), len(grid[0])
        change = False
        toBeRot = []
        for r in range(n_row):
            for c in range(n_col):
                if grid[r][c] == 2:
                    if r-1 >= 0:
                        if grid[r-1][c] == 1:
                            # grid[r-1][c] = 2
                            toBeRot.append([r-1, c])
                            change = True
                    if r+1 < n_row:
                        if grid[r+1][c] == 1:
                            # grid[r+1][c] = 2
                            toBeRot.append([r+1, c])
                            change = True
                    if c-1 >= 0:
                        if grid[r][c-1] == 1:
                            # grid[r][c-1] = 2
                            toBeRot.append([r, c-1])
                            change = True
                    if c+1 < n_col:
                        if grid[r][c+1] == 1:
                            # grid[r][c+1] = 2
                            toBeRot.append([r, c+1])
                            change = True
        for (r, c) in toBeRot:
            grid[r][c] = 2
        return change


    def checkRot(grid):
        n_row, n_col = len(grid), len(grid[0])
        # allRot = True
        for r in range(n_row):
            for c in range(n_col):
                if grid[r][c] == 1:
                    # allRot = False
                    return False
        return True

    result = 0
    while True:
        if checkRot(grid):
            return result
        if rot(grid):
            result += 1
        else:
            return -1


# Test cases
if __name__ == "__main__":
    test_cases = [
        (
            [
                [2, 1, 1],
                [1, 1, 0],
                [0, 1, 1],
            ],
            4,
        ),
        (
            [
                [2, 1, 1],
                [0, 1, 1],
                [1, 0, 1],
            ],
            -1,
        ),
        (
            [
                [0, 2],
            ],
            0,
        ),
        (
            [[1]],
            -1,
        ),
        (
            [[2]],
            0,
        ),
        (
            [
                [2, 1],
                [1, 1],
                [1, 2],
            ],
            1,
        ),
    ]

    print("=" * 70)
    print("LeetCode 994 - Rotting Oranges")
    print("=" * 70)

    for grid, expected in test_cases:
        try:
            grid_copy = [row[:] for row in grid]
            result = orangesRotting(grid_copy)
            if result is None:
                print(f"⚠️  grid={grid} -> Not implemented")
            else:
                is_correct = result == expected
                status = "✓" if is_correct else "✗"
                print(f"{status} grid (m={len(grid)}, n={len(grid[0])})")
                print(f"   Output: {result}, Expected: {expected}")
        except Exception as e:
            print(f"❌ grid={grid} -> Error: {e}")

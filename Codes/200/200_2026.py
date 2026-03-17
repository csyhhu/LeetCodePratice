"""
[200] Number of Islands
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid representing a map, where '1' represents land and '0' represents water,
return the number of islands. An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

Example 1:
    Input: grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    Output: 1

Example 2:
    Input: grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    Output: 3

Example 3:
    Input: grid = [
        ["1","1","1"],
        ["0","1","0"],
        ["1","1","1"]
    ]
    Output: 1

Constraints:
    - m == grid.length
    - n == grid[i].length
    - 1 <= m, n <= 300
    - grid[i][j] is '0' or '1'

Date: 2026-03-08
"""


def numIslands(grid):
    """
    Count the number of islands in a 2D grid.
    
    Args:
        grid: List[List[str]] - 2D grid where '1' is land and '0' is water
    
    Returns:
        int - Number of islands
    """
    pass


# Test cases
if __name__ == "__main__":
    test_cases = [
        (
            [
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ],
            1
        ),
        (
            [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ],
            3
        ),
        (
            [
                ["1","1","1"],
                ["0","1","0"],
                ["1","1","1"]
            ],
            1
        ),
        (
            [
                ["0"]
            ],
            0
        ),
        (
            [
                ["1"]
            ],
            1
        ),
        (
            [
                ["1","0","1"],
                ["1","0","1"],
                ["1","0","1"]
            ],
            3
        ),
    ]
    
    print("=" * 70)
    print("LeetCode 200 - Number of Islands")
    print("=" * 70)
    
    for grid, expected in test_cases:
        try:
            # Make a copy to avoid modifying the original
            grid_copy = [row[:] for row in grid]
            result = numIslands(grid_copy)
            if result is None:
                print(f"⚠️  grid={grid} -> Not implemented")
            else:
                is_correct = result == expected
                status = "✓" if is_correct else "✗"
                print(f"{status} grid (m={len(grid)}, n={len(grid[0])})")
                print(f"   Output: {result}, Expected: {expected}")
        except Exception as e:
            print(f"❌ grid={grid} -> Error: {e}")

"""
LeetCode 149: Max Points on a Line
https://leetcode.com/problems/max-points-on-a-line/

Given an array of points where points[i] = [xi, yi] represents a point on 
the X-Y plane, return the maximum number of points that lie on the same 
straight line.

Example 1:
    Input: points = [[1,1],[2,2],[3,3]]
    Output: 3

Example 2:
    Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    Output: 4

Constraints:
    - 1 <= points.length <= 300
    - points[i].length == 2
    - -10^4 <= xi, yi <= 10^4
    - All the points are unique.

Hints:
    - For each point, compute the slope to every other point.
    - How do you represent a slope exactly (without floating point error)?
    - What special cases exist? (vertical line, duplicate points)
    - GCD can help you normalize a slope fraction.
"""
from collections import defaultdict
from math import gcd


def maxPoints(points: list[list[int]]) -> int:
    """
    For each point as anchor, count how many other points share the same slope.
    Use a reduced fraction (dy/gcd, dx/gcd) as the slope key to avoid float issues.

    Args:
        points: List of [x, y] coordinates

    Returns:
        Maximum number of collinear points
    """
    # print(gcd(0, 4))
    n = len(points)
    max_same_slope = 0
    for i in range(n):
        slope_dict = {}
        cur_max_same_slop = 0
        for j in range(n):
            if i == j:
                continue
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            g = gcd(abs(dx), abs(dy))
            key = (dx / g, dy / g)
            if key not in slope_dict:
                slope_dict[key] = 0
            slope_dict[key] += 1
            cur_max_same_slop = max(cur_max_same_slop, slope_dict[key])
        max_same_slope = max(max_same_slope, cur_max_same_slop)
    return max_same_slope + 1
        
    


# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "input": [[1, 1], [2, 2], [3, 3]],
            "expected": 3,
            "description": "All three points on y=x",
        },
        {
            "input": [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]],
            "expected": 4,
            "description": "4 points on a line among 6",
        },
        {
            "input": [[1, 1]],
            "expected": 1,
            "description": "Single point",
        },
        {
            "input": [[1, 1], [2, 2]],
            "expected": 2,
            "description": "Two points always on a line",
        },
        {
            "input": [[0, 0], [1, 0], [2, 0], [0, 1], [0, 2]],
            "expected": 3,
            "description": "Horizontal line (3 points) and vertical line (3 points)",
        },
        {
            "input": [[0, 0], [0, 1], [0, 2], [0, 3]],
            "expected": 4,
            "description": "Vertical line - all 4 on x=0",
        },
        {
            "input": [[2, 3], [3, 3], [-5, 3]],
            "expected": 3,
            "description": "Horizontal line y=3",
        },
    ]

    print("=" * 65)
    print("LeetCode 149: Max Points on a Line - Test Results")
    print("=" * 65)

    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        result = maxPoints(test["input"])
        is_pass = result == test["expected"]
        status = "✅ PASS" if is_pass else "❌ FAIL"

        if is_pass:
            passed += 1
        else:
            failed += 1

        print(f"\nTest Case {i}: {status}")
        print(f"  Description: {test['description']}")
        print(f"  Input:       {test['input']}")
        print(f"  Expected:    {test['expected']}")
        print(f"  Your Output: {result}")

    print("\n" + "=" * 65)
    print(f"Summary: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 65)

    if failed == 0:
        print("🎉 All test cases passed!")
    else:
        print(f"⚠️  {failed} test case(s) failed. Please review.")

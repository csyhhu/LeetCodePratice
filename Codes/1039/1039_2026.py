"""
LeetCode 1039: Minimum Score Triangulation of Polygon

Problem Description:
You have a convex n-gon (a polygon with n vertices in order). You must triangulate 
the n-gon into (n - 2) triangles using (n - 3) non-crossing diagonals.

For each triangle, the score is the product of the lengths of its sides. 
The score of a triangulation is the sum of the scores of its triangles.

Return the minimum score possible for a triangulation of the n-gon.

Example:
Input: values = [1,2,3]
Output: 6
Explanation: The polygon is a triangle. One possible triangulation (with no diagonals) 
is giving the triangle with score 1*2*3 = 6.

Input: values = [3,7,4,5]
Output: 144
Explanation: There are two triangulations of a 4-gon. Calculate both triangulations' 
value and return the minimum one. In this case, both triangulations with scores 
3*7*5 + 7*4*5 = 140 and 3*7*4 + 3*4*5 = 144 satisfy the problem's requirements.

Constraints:
- n == values.length
- 3 <= n <= 50
- 1 <= values[i] <= 100

Related Topics:
- Dynamic Programming
- Math
- Interval DP
"""


def minScoreTriangulation(values: list[int]) -> int:
    """
    Find the minimum score possible for a triangulation of an n-gon.
    
    Args:
        values: List of side lengths of the polygon in order
        
    Returns:
        The minimum possible triangulation score
    """
    # TODO: Your implementation here
    # dp[i,j] = min(dp[i, k] + dp[k, j])
    n = len(values)
    dp = [[0] * n for _ in range(n)]
    # print(dp)
    for length in range(2, n):
        for i in range(n - length):
            j = i + length
            dp[i][j] = 101 * 101 * 101
            for k in range(i + 1, j):
                # print(i, k, j)
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + values[i] * values[k] * values[j])

    return dp[0][n - 1]

# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "input": [1, 2, 3],
            "expected": 6,
            "description": "Simple triangle (no diagonals needed)",
            "explanation": "Only one triangle: 1 × 2 × 3 = 6"
        },
        {
            "input": [3, 7, 4, 5],
            "expected": 144,
            "description": "Quadrilateral - Standard example",
            "explanation": "Diagonal 0-2: (0,1,2)=3×7×4=84 + (0,2,3)=3×4×5=60 = 144"
        },
        {
            "input": [1, 3, 1, 2, 2],
            "expected": 9,
            "description": "Pentagon - 5 vertices",
            "explanation": "Optimal triangulation yields score 9"
        },
        {
            "input": [2, 1, 4, 3],
            "expected": 18,
            "description": "Quadrilateral - Second example",
            "explanation": "Diagonal 1-3: (0,1,3)=2×1×3=6 + (1,2,3)=1×4×3=12 = 18"
        },
        {
            "input": [5, 5, 5],
            "expected": 125,
            "description": "Equilateral triangle",
            "explanation": "Only one triangle: 5 × 5 × 5 = 125"
        }
    ]
    
    print("=" * 70)
    print("LeetCode 1039: Minimum Score Triangulation of Polygon - Test Results")
    print("=" * 70)
    print()
    
    passed = 0
    failed = 0
    
    for i, test in enumerate(test_cases, 1):
        result = minScoreTriangulation(test["input"])
        is_pass = result == test["expected"]
        status = "✅ PASS" if is_pass else "❌ FAIL"
        
        if is_pass:
            passed += 1
        else:
            failed += 1
        
        print(f"Test Case {i}: {status}")
        print(f"  Description: {test['description']}")
        print(f"  Input:       {test['input']}")
        print(f"  Expected:    {test['expected']}")
        print(f"  Your Output: {result}")
        print(f"  Explanation: {test['explanation']}")
        print()
    
    print("=" * 70)
    print(f"Summary: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 70)
    
    if failed == 0:
        print("🎉 Excellent! All test cases passed!")
    else:
        print(f"⚠️  {failed} test case(s) failed. Please review the output above.")

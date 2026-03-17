"""
[11] Container With Most Water
https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines drawn such that
the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container
contains the most water.

Return the maximum area of water the container can store.

Notice that you may not slant the container.

Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The vertical lines are at index 1 and 8.
    Area = min(height[1], height[8]) * (8 - 1) = min(8, 7) * 7 = 7 * 7 = 49

Example 2:
    Input: height = [2,3,4,5,4,3,2]
    Output: 12

Constraints:
    - n == height.length
    - 2 <= n <= 10^5
    - 0 <= height[i] <= 10^4

Key Insights (关键洞察):
    - 面积公式: area = min(height[left], height[right]) * (right - left)
    - 暴力法: O(n^2) - 枚举所有两个柱子的组合
    - 优化: 用双指针从两端向中间移动，O(n) 时间复杂度
    - 关键: 每次应该移动较矮的那个指针，为什么？
        * 如果移动较高的指针，宽度减少，矮的指针还是它，面积肯定减小
        * 只有移动较矮的指针，才有可能找到更高的，面积才有可能增加

Date: 2026-03-02
"""

def maxArea(height):
    """
    思路：
    双指针法：从两端开始，每次移动较矮的边
    
    TODO: 实现这个函数
    步骤：
    1. 初始化left=0, right=len(height)-1
    2. 初始化max_area=0
    3. 当left < right时：
       - 计算当前面积
       - 更新max_area
       - 比较height[left]和height[right]，移动较矮的指针
    4. 返回max_area
    
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    max_area = 0
    n = len(height)
    i = 0
    j = n - 1
    while i < j:
        area = min(height[i], height[j]) * (j - i)
        max_area = max(max_area, area)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_area



def maxArea_brute_force(height):
    """
    暴力法：
    枚举所有可能的两个柱子的组合
    
    TODO: 实现这个函数（简单但不高效）
    
    时间复杂度：O(n^2)
    空间复杂度：O(1)
    """
    n = len(height)
    dp = [[0] * n for _ in range(n)]
    dp[0][n-1] = min(height[0], height[n-1]) * (n-1)
    max_area = 0
    for i in range(0, n-1):
        for j in range(n-1, i, -1):
            # print(i, j)
            left_area = min(height[i+1], height[j]) * (j - i - 1)
            right_area = min(height[i], height[j-1]) * (j - 1 - i)
            dp[i][j] = max(dp[i][j], dp[i+1][j], left_area, right_area)
            max_area = max(max_area, dp[i][j])
    return max_area


def maxArea_traced(height):
    """
    双指针法（带过程追踪）：
    显示每一步的选择，方便理解算法过程
    
    TODO: 实现这个函数
    返回值：(最大面积, 步骤列表)
    每个步骤应该记录：left, right, height[left], height[right], 当前面积
    
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    pass


# Test cases
if __name__ == "__main__":
    # Test case 1
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result1 = maxArea(height1)
    print(f"Input: {height1}")
    print(f"Output: {result1}")
    print(f"Expected: 49\n")

    # Test case 2
    height2 = [2, 3, 4, 5, 4, 3, 2]
    result2 = maxArea(height2)
    print(f"Input: {height2}")
    print(f"Output: {result2}")
    print(f"Expected: 12\n")

    # Test case 3
    height3 = [1, 1]
    result3 = maxArea(height3)
    print(f"Input: {height3}")
    print(f"Output: {result3}")
    print(f"Expected: 1\n")

    # Test case 4
    height4 = [0, 2]
    result4 = maxArea(height4)
    print(f"Input: {height4}")
    print(f"Output: {result4}")
    print(f"Expected: 0\n")

    # Test brute force
    # print("=" * 50)
    # print("Testing brute force method:")
    # print("=" * 50)
    # result_brute = maxArea_brute_force(height1)
    # print(f"Brute force result: {result_brute}")
    # print(f"Optimized result: {result1}")
    # print(f"Match: {result_brute == result1}\n")

    # Show detailed steps
    # print("=" * 50)
    # print("Detailed steps for example 1:")
    # print("=" * 50)
    # max_area, steps = maxArea_traced(height1)
    # if steps:
    #     print(f"Height array: {height1}")
    #     print(f"Steps:")
    #     for i, step in enumerate(steps):
    #         print(f"  Step {i+1}: left={step.get('left')}, right={step.get('right')}, "
    #               f"h[{step.get('left')}]={step.get('h_left')}, "
    #               f"h[{step.get('right')}]={step.get('h_right')}, "
    #               f"area={step.get('area')}")
    #     print(f"Max area: {max_area}\n")

    # Edge cases
    print("=" * 50)
    print("Edge cases:")
    print("=" * 50)
    edge_cases = [
        ([1, 1], 1),
        ([1, 2, 4, 3], 4),
        ([2, 1, 1, 1, 1], 4),
        ([9, 3, 4, 7, 2, 12, 6], 45),
    ]
    
    for test_input, expected in edge_cases:
        result = maxArea(test_input)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {test_input}, Output: {result}, Expected: {expected}")

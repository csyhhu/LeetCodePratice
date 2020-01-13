def maxArea(height):
    left = 0
    right = len(height) - 1
    results = 0
    while left <= right:
        # print(left, right)
        area = min(height[left], height[right]) * (right - left)
        results = max(results, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return results

inputs = [1,8,6,2,5,4,8,3,7]
print(maxArea(inputs))
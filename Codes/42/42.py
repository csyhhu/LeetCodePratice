def trap_brute_force(height):

    n = len(height)
    ans = 0
    for i in range(1, n-1):
        min_height = min(max(height[0:i]), max(height[i+1:]))
        if min_height > height[i]:
            ans += (min_height - height[i])
    return ans

def trap_dp(height):
    n = len(height)
    if n == 0:
        return 0
    left_max = [0] * n
    left_max[0] = height[0]
    right_max = [0] * n
    right_max[n-1] = height[n-1]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
    ans = 0
    for i in range(1, n-1):
        min_height = min(right_max[i+1], left_max[i-1])
        if min_height > height[i]:
            ans += (min_height - height[i])
    return ans

def trap(height):
    n = len(height)
    if n == 0:
        return 0
    left_max = height[0]
    right_max = height[n-1]
    l_pointer = 1
    r_pointer = n-2
    ans = 0
    while l_pointer <= r_pointer:
        if left_max < right_max:
            area = left_max - height[l_pointer]
            ans += (area if area > 0 else 0)
            left_max = max(left_max, height[l_pointer])
            l_pointer += 1
        else:
            area = right_max - height[r_pointer]
            ans += (area if area > 0 else 0)
            right_max = max(right_max, height[r_pointer])
            r_pointer -= 1

    return ans

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))
def canJump_dfs(nums):

    possible = [True] * len(nums)

    def dfs(start):
        if start > len(nums) - 1:
            return False
        if start == len(nums) - 1:
            return True
        if not possible[start]:
            return False
        if nums[start] == 0:
            possible[start] = False
            return False
        num_steps = nums[start]
        for i in range(num_steps, 0, -1):
            if dfs(start + i):
                return True
        possible[start] = False
        return False

    return dfs(0)

def canJump(nums):

    far = 0
    for i, num in enumerate(nums):
        if far < i:
            return False
        if far >= len(nums) - 1:
            return True
        far = max(far, num + i)

nums = [2,3,1,1,4]
print(canJump(nums))

nums = [3,2,1,0,4]
print(canJump(nums))
def permuteUnique(nums):
    result = []
    def dfs(nums, used, cur, res):
        if len(cur) == len(nums):
            if cur not in res:
                res.append(cur.copy())
            return
        for idx in range(len(nums)):
            if not used[idx]:
                cur.append(nums[idx])
                used[idx] = True
                dfs(nums, used, cur, res)
                used[idx] = False
                cur.pop()

    used = [False] * len(nums)

    dfs(nums, used, [], result)
    return result


def permuteUnique2(nums):
    nums = sorted(nums)
    result = []

    def dfs(nums, used, cur, res):
        if len(cur) == len(nums):
            res.append(cur.copy())
            return
        for idx in range(len(nums)):
            if used[idx]:
                continue
            if idx > 0 and nums[idx] == nums[idx-1] and used[idx-1]:
                continue
            cur.append(nums[idx])
            used[idx] = True
            dfs(nums, used, cur, res)
            used[idx] = False
            cur.pop()

    used = [False] * len(nums)

    dfs(nums, used, [], result)
    return result

nums = [1,2,3]
print(permuteUnique2(nums))

nums = [1,1,2]
print(permuteUnique2(nums))
import copy

def permute(nums):
    n  = len(nums)
    results = []
    used = [0] * n
    def dfs(step, cur):
        if step == n:
            results.append(copy.deepcopy(cur))
            return
        for idx, val in enumerate(nums):
            if used[idx]:
                continue
            cur.append(val)
            used[idx] = 1
            dfs(step + 1, cur)
            cur.pop()
            used[idx] = 0
        return results
    return dfs(0, [])

inputs = [1,2,3]
print(permute(inputs))
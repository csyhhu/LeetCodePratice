def combination(nums):

    results = []

    def dfs(n, s, cur):
        if len(cur) == n:
            results.append(cur.copy())
            return
        for idx in range(s, len(nums)):
            cur.append(nums[idx])
            dfs(n, idx + 1, cur)
            cur.pop()

    for i in range(len(nums)+1):
        dfs(i, 0, [])

    return results


def permutation(nums):

    results = []
    used = [False] * len(nums)

    def dfs(n, s, cur):
        if len(cur) == n:
            results.append(cur.copy())
            return
        for idx in range(0, len(nums)):
            if used[idx]:
                continue
            cur.append(nums[idx])
            used[idx] = True
            dfs(n, s+1, cur)
            cur.pop()
            used[idx] = False

    for i in range(len(nums)+1):
        dfs(i, 0, [])

    return results


def subsets(nums):

    n = len(nums)
    # return [[nums[i] for i in range(n) if s & 1 << i > 0] for s in range(1 << n)]
    results = []
    for s in range(1 << n): # 0,...,31
        cur = []
        for i in range(n): # 0,...,5: Find out 1 in s
            if s & (1 << i) > 0: # whether the i index in s is 1
                cur.append(nums[i])
        results.append(cur)
    return results

print(combination([1,2,3,4]))
# print(permutation([1,2,3,4]))

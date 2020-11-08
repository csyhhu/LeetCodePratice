def combine(n, k):

    results = []
    def dfs(start, curCombination):
        if len(curCombination) == k:
            results.append(curCombination.copy())
            return
        for i in range(start, n + 1):
            curCombination.append(i)
            dfs(i + 1, curCombination)
            curCombination.pop(-1)

    dfs(1, [])
    return results

n = 4
k = 2
print(combine(n, k))
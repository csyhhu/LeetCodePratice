def mctFromLeafValues(arr):
    # dp = [10e9] * len(arr)
    dp = [0] * len(arr)
    dp[0] = 0
    dp[1] = arr[0] * arr[1]
    # dp = [0] * len(arr)
    # dp[0] = 0
    # dp[1] = arr[0] * arr[1]
    for i in range(2, len(arr)):
        dp[i] = min(dp[i-1] + max(arr[0: i]) * arr[i],
                    dp[i-2] + max(arr[0: i-1]) * max(arr[i-1], arr[i]) + arr[i-1] * arr[i])
    print(dp)
    return dp[-1]


def mctFromLeafValues2(arr):

    # dp = [[1e9] * len(arr)] * len(arr)
    memory = {}
    # dfs(start, end): the desired answer given arr[start: end+1]
    def dfs(start, end):
        if end <= start:
            return 0
        if (start, end) in memory:
            return memory[(start, end)]
        res = float('inf')
        for k in range(start+1, end+1):
            res = min(res, dfs(start, k-1) + dfs(k, end) + max(arr[start: k]) * max(arr[k: end+1]))
            memory[(start, end)] = res
        return res

    return dfs(0, len(arr) - 1)


# arr = [6,2,4]
arr = [15, 13, 5, 3, 15]
outputs = mctFromLeafValues2(arr)
print(outputs)
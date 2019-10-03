def stoneGameII(piles):
    n = len(piles)
    from functools import lru_cache
    @lru_cache(None)
    def dfs(x, M):
        if x + 2 * M >= n:
            return sum(piles[x:])
        res = float('-inf')
        for i in range(1, 2*M+1): # Try M=1, i \in [1,2,3)
            res = max(res, sum(piles[x:x+i]) - dfs(x + i, max(i, M)))
        return res

    diff = dfs(0, 1)
    return (sum(piles) + diff)//2

def stoneGameII2(piles):

    n = len(piles)
    dp = [[0] * n for _ in range(n)]
    # print(dp)
    for i in range(n):
        for M in range(n):
            if i + 2 * (M) >= n:
                print(i, M)
                dp[i][M] = sum(piles[i:])
            # else:
            #     dp[i][M] = 0
    # print(dp)

    for i in range(n-1, -1, -1):
        for M in range(n-1, -1, -1):
            # if i + 2 * (M + 1) >= n:
            #     continue
            for x in range(0, 2*M+1):
                if i+x >= n:
                    continue
                dp[i][M] = max(dp[i][M], sum(piles[i:i+x]) - dp[i+x][max(x, M)])
    #
    # print(dp)
    return dp[0][1]


piles = [2,7,9,4,4]
outputs = stoneGameII2(piles)
print(outputs)
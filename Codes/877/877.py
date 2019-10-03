def stoneGame(piles):
    n = len(piles)
    dp = [[0]*n]*n
    # dp[i][j]: with the remaining piles from i to j (included), the maximum score [gap] that
    # the first player can get
    for i in range(n):
        dp[i][i] = piles[i]

    for i in range(n):
        for l in range(2, n - i):
            j = i + l - 1
            dp[i][j] = max(piles[i] - dp[i+1][j],
                           piles[j] - dp[i][j-1])

    # print(dp)
    return dp[0][n-1]>0

inputs = [5,3,4,5]
outputs = stoneGame(inputs)
print(outputs)
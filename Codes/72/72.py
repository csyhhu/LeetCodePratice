def minDistance(word1: str, word2: str):

    n, m = len(word1), len(word2)
    # Given word1 with i words and word2 with j words, the minimal number of actions required to convert word1 to word2
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n+1):
        dp[i][0] = i
    for j in range(1, m+1):
        dp[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Correspond to replace, delete words[i], delete words[j]
                dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1

    return dp[n][m]

print(minDistance(word1 = "horse", word2 = "ros"))
print(minDistance(word1 = "intention", word2 = "execution"))
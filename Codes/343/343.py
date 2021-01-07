def integerBreak(n: int) -> int:

    dp = [1] * 58
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    for i in range(4, n + 1):
        for m in range(1, i // 2 + 1):
            dp[i] = max(
                dp[i],
                max(dp[m], m) * max(dp[i - m], i-m)
            )
    print(dp[:n+1])
    return dp[n]

# print(integerBreak(2))
print(integerBreak(8))
print(integerBreak(10))

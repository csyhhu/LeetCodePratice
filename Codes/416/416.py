def canPartition(nums):

    n = len(nums)
    if sum(nums) % 2 == 1:
        return False
    target = sum(nums) // 2
    # dp[i][j]: With the first i nums available, whether we can get a summation of j
    """
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    for i in range(n):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(nums[i-1], target + 1):
            # When nums[i] is added, whether we can achieve target can be divided into:
            # 1. Don't add nums[i]
            # 2. Add nums[i]
            dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
    """
    dp = [[False] * (target + 1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = True
    for i in range(n):
        # It should starts from nums[i], otherwise j-nums[i] will be negative
        for j in range(nums[i], target+1):
            dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]

    # print(dp)
    return dp[n-1][target]

print(canPartition(nums = [1,5,11,5]))
print(canPartition(nums = [1,2,3,5]))
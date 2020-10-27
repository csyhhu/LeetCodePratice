def maxSubArray(nums):

    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)
    # dp[0] = nums[0]

    for i, num in enumerate(nums):
        if i == 0:
            dp[i] = nums[i]
        else:
            dp[i] = max(dp[i-1] + num, num)

    # print(dp)

    return max(dp)

nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(maxSubArray(nums))

nums = [-2,-1]
print(maxSubArray(nums))
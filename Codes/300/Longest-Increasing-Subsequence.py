def lengthOfLIS_wrong_understanding(nums):
    if len(nums) == 0:
        return 0

    left = 0
    right = 0
    max_len = 1
    while right < len(nums) - 1:

        if nums[right] < nums[right + 1]:
            right += 1
            max_len = max(max_len, right - left + 1)
        else:
            max_len = max(max_len, right - left + 1)
            right += 1
            left = right

        right += 1

    return max_len

def lengthOfLIS(nums):

    if len(nums) == 0:
        return 0

    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

inputs = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(inputs))
inputs = [2,2]
print(lengthOfLIS(inputs))
inputs = [1,3,6,7,9,4,10,5,6]
print(lengthOfLIS(inputs))
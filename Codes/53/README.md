# Description

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Solution
`dp[i]`: 包含`nums[i]`的最大和的子序列之和。

`dp[i] = dp[i-1] + nums[i], nums[i]`: 若新增一个数`nums[i]`，判断该数加进来之后的和，与以该数重开一个新子数组，哪一个和更大。
最终输出`max(dp)`.
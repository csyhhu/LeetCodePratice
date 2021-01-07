# Description

Given an array `nums`, find out the number of subarrays that contain exactly `k` odd numbers.

# Solution

## 前缀和
用一个`dict: num_odd`记录下：`num_odd[i]`: 包含`i`个奇数的以`0`为起点的区间。遍历数组，记录下当前数组的奇数总数量`cur_odd_sum`，然后用`cur_odd_sum-k`去检索前方是否存在这样的区间，如果有，说明以当前这个index为左起点，前方存在若干个右起点，其和index组成的子区间有`k`个奇数。

同时更新`num_odd[cur_odd_sum] = num_odd[cur_odd_sum] + 1`
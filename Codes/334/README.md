# Solution

## Solution 1
[最长上升子序列](../../Codes/300)这道题中有个很tricky的解法：保存一个list，对于一个新增加的数num，如果该数大于list中最后一个，则加进去；否则在list中找到第一个比该数大的数，并用num替换。
list的长度即为最长上升子序列的长度。在这里关键是找出list中第一个比num大的数，可以用二分来加速。但在这道题里list最长是3，所以可以认为是常数，故直接使用，时间复杂度还是o(N).

## Solution 2
在网上看到一个挺有意思的解法：

保持两个数组forward和backward. forward[i]：nums[1: i] (注意这里不包括i)中最小元素，backward[i]: nums[0: i-1] (注意这里不包括i-1)中最小元素.
然后从nums[1:n]开始遍历，如果满足forward[j] < nums[j] < backward[j]，则说明存在这样的三元组。

举例：
[1,2,3,4,5]

forward:  [X, 1, 1, 1, 1]

backward: [5, 5, 5, 5, X]

注意forward的第一个和backward的最后一个元素我们都不需要管，因为nums不需要遍历到这两个元素。而nums中的2，3，4满足条件。故可以。

但这种解法空间复杂度是o(N)，不满足题意。
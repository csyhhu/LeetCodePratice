# 33. Search in Rotated Sorted Array

You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`).

If target is found in the array return its index, otherwise, return `-1`.

## Solution
二分的思路：取`start`, `mid`, `end`. 分类讨论：
- 如果`nums[start]<=nums[mid]`, 说明`[start, mid]`是有序的。
    - 若`nums[start]<=target<nums[mid]`，则说明`target`在一个有序序列中，继续用二分即可解决：`end=mid-1`.
    - 若上面不符合，说明`target`不在这个有序序列中，去另一边的序列里找：`start = mid + 1`.
- else, 说明`[mid, end]`是有序的。之后处理如上。
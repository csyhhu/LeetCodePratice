# Description

# Solution
- Min-heap to find the kth largest number
- Quick selection

## Quick Selection 1
- 做快速排序，但只需要把大于pivot的放到pivot**右边**，小的放在**左边**。
- 返回当前pivot的下标(mid)，表示pivot是当前数组第mid大的值。如果该值等于k-1，即说明当前pivot是第k大的。
- 若该值小于k-1, 则说明pivot值太大了，第k大在pivot左边的数组中。把该数组传入继续计算，同时更新k-1为k-1-mid, 因为在左区间中，我们已经不需要找那么多的数了，前mid个大的数已经被我们找出来了。
- 若该值小于k-1，则说明第k大在pivot右边的数组中。把该数组传入继续计算，不需要更改k值。

## Quick Selection 2
- 做快速排序，但只需要把大于pivot的放到pivot**左边**，小的放在**右边**。
- 返回当前pivot的下标(mid)，表示pivot是当前数组第mid大的值。如果该值等于k-1，即说明当前pivot是第k大的。
- 若该值小于k-1, 则说明pivot值太大了，第k大在pivot右边的数组中，因此更新数组左节点为`mid+1`
- 反之，更新右节点为`mid-1`.
- 注意，这么做不会影响结果，因为每次都在一个无序的区间做伪快排。
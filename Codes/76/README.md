# Description
给定两个字符串`s`,`t`,求`s`中包含所有`t`中的字符串的最短区间。

# Solution

## Two Pointers
`left`,`right`两个pointer指向区间开始和结束。`right`先向后移动，直到找到能覆盖全部`t`中的字符的区间。然后`left`开始移动，不断减掉区间中的字符，直到刚好刚好可以覆盖。
此时更新最小区间的首尾。然后`right`/`left`再移动，直到遍历整个字符串。
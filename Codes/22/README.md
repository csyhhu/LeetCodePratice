# 22. Generate Parentheses

## Description
Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

## Solution

### Sol1
递归思路：构造一个递归函数，入参有两个：`left`, `right`,分别表示当前还剩下的左右括号。
很显然，当`left=0`and`right=0`时，返回结果；
当`left>right`时，出现非法括号，返回但不把当前结果加入最终结果list中；
当`left<right`时，我们可以往后面加一个`(`,同时`left-1`;或者加入一个`)`,同时`right-1`,并进入下一层递归。

### Sol2
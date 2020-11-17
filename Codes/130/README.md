# Description

Given a 2D board containing `X` and `O` (the letter `O`), capture all regions surrounded by `X`.

A region is captured by flipping all `O`s into `X`s in that surrounded region.

# Solution

- 扫描矩阵四条边，如果有`O`，则用 DFS 遍历，将所有连着的`O`都变成另一个字符，比如`$`，这样剩下的`O`都是被包围的，然后将这些`O`变成`X`，把`$`变回`O`就行了。

- 扫描矩阵四条边，如果有`O`，则将其置为`#`. 接着使用DFS, 记录每次DFS的路径。设置一个是否flip的flag. 执行完整的DFS找出联通的`O`. 如果路径上存在`#`，就不执行反转；否则就将路径上的点都反转。
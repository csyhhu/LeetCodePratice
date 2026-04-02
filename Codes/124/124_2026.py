"""
[124] Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/

A path in a binary tree is a sequence of nodes where each pair of adjacent
nodes in the sequence has an edge connecting them. A node can only appear in
the sequence AT MOST ONCE. Note that the path does not need to pass through
the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any
non-empty path.

Example 1:
        1
       / \
      2   3

    Input: root = [1, 2, 3]
    Output: 6
    Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
       -10
       /  \
      9   20
         /  \
        15   7

    Input: root = [-10, 9, 20, None, None, 15, 7]
    Output: 42
    Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Constraints:
    - The number of nodes in the tree is in the range [1, 3 * 10^4].
    - -1000 <= Node.val <= 1000

Hint:
    - 思考 DFS 函数的「返回值」和「副作用」分别表示什么含义
    - 递归函数返回的是：经过当前节点、只能延伸到一侧子树的最大贡献值
    - 全局答案（路径可以同时拐弯经过左右两侧）需要在递归过程中单独维护

Date: 2026-03-27
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root: TreeNode) -> int:
    res = float("-inf")

    def dfs(_node):
        nonlocal res
        if not _node:
            return 0
        
        left_gain = max(dfs(_node.left), 0)
        right_gain = max(dfs(_node.right), 0)

        res = max(res, _node.val + left_gain + right_gain)
        return _node.val + max(left_gain, right_gain)
    
    dfs(root)
    return res


# ─────────────────────────────────────────────
# 工具函数：方便测试
# ─────────────────────────────────────────────

def build_tree(vals):
    """按层序（BFS 顺序）构建二叉树，None 表示空节点"""
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = [root]
    i = 1
    while queue and i < len(vals):
        node = queue.pop(0)
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


# Test cases
if __name__ == "__main__":
    test_cases = [
        # (tree_vals, expected)
        ([1, 2, 3], 6),
        ([-10, 9, 20, None, None, 15, 7], 42),
        ([-3], -3),
        ([1, -2, -3, 1, 3, -2, None, -1], 3),
    ]

    for tree_vals, expected in test_cases:
        root = build_tree(tree_vals)
        result = maxPathSum(root)
        status = "✓" if result == expected else "✗"
        print(f"{status} tree={tree_vals}")
        print(f"   Output:   {result}")
        print(f"   Expected: {expected}\n")

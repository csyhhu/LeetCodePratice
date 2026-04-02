"""
[543] Diameter of Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges
between them.

Example 1:
          1
         / \\
        2   3
       / \\
      4   5

    Input: root = [1, 2, 3, 4, 5]
    Output: 3
    Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
    Input: root = [1, 2]
    Output: 1

Constraints:
    - The number of nodes in the tree is in the range [1, 10^4].
    - -100 <= Node.val <= 100

Hint:
    - 这道题和 124 题是同构的，思考一下 DFS 的「返回值」和「全局答案」分别是什么
    - 递归函数返回的是：以当前节点为端点，能向下延伸的最大深度（边数）
    - 全局答案：经过当前节点时，左深度 + 右深度（可以拐弯）

Date: 2026-03-28
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root: TreeNode) -> int:

    res = float('-inf')

    def dfs(_node):
        nonlocal res
        if not _node:
            return 0
        left_depth = dfs(_node.left)
        right_depth = dfs(_node.right)
        cur_depth = max(left_depth, right_depth) + 1
        res = max(res, left_depth + right_depth)
        return cur_depth

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
        ([1, 2, 3, 4, 5], 3),
        ([1, 2], 1),
        ([1], 0),
        ([1, 2, None, 3, None, 4, None, 5], 4),  # 线形树，直径为4
    ]

    for tree_vals, expected in test_cases:
        root = build_tree(tree_vals)
        result = diameterOfBinaryTree(root)
        status = "✓" if result == expected else "✗"
        print(f"{status} tree={tree_vals}")
        print(f"   Output:   {result}")
        print(f"   Expected: {expected}\n")

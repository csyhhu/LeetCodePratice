"""
[236] Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
in the tree.

According to the definition of LCA on Wikipedia: "The lowest common ancestor
is defined between two nodes p and q as the lowest node in T that has both p
and q as descendants (where we allow a node to be a descendant of itself)."

Example 1:
         3
        / \
       5   1
      / \ / \
     6  2 0  8
       / \
      7   4

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3
    Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5
    Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a
                 descendant of itself according to the LCA definition.

Example 3:
    Input: root = [1,2], p = 1, q = 2
    Output: 1

Constraints:
    - The number of nodes in the tree is in the range [2, 10^5].
    - -10^9 <= Node.val <= 10^9
    - All Node.val are unique.
    - p != q
    - p and q will exist in the tree.

Date: 2026-03-25
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root, p, q):
    """
    时间复杂度：O(n)
    空间复杂度：O(h)，h 为树高
    """
    if root is None or root == p or root == q:
        return root
        
    left = lowestCommonAncestor(root.left, p, q) # Determine whether root.left contain p or q
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    else:
        return left or right


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


def find_node(root, val):
    """在树中找到值为 val 的节点"""
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


# Test cases
if __name__ == "__main__":
    test_cases = [
        # (tree_vals, p_val, q_val, expected_val)
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5),
        ([1, 2], 1, 2, 1),
    ]

    for tree_vals, p_val, q_val, expected_val in test_cases:
        root = build_tree(tree_vals)
        p = find_node(root, p_val)
        q = find_node(root, q_val)
        result = lowestCommonAncestor(root, p, q)
        result_val = result.val if result else None
        status = "✓" if result_val == expected_val else "✗"
        print(f"{status} p={p_val}, q={q_val}")
        print(f"   Output:   {result_val}")
        print(f"   Expected: {expected_val}\n")

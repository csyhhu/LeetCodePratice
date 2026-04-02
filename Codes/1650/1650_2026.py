"""
[1650] Lowest Common Ancestor of a Binary Tree III
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node in the tree contains a `parent` pointer that points to its parent node.
The root node's parent is null.

According to the definition of LCA on Wikipedia: "The lowest common ancestor of
two nodes p and q in a tree T is the lowest node that has both p and q as
descendants (where we allow a node to be a descendant of itself)."

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

Example 2:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5

Example 3:
    Input: root = [1,2], p = 1, q = 2
    Output: 1

Constraints:
    - The number of nodes in the tree is in the range [2, 10^5].
    - -10^9 <= Node.val <= 10^9
    - All Node.val are unique.
    - p != q
    - p and q exist in the tree.
    - Each node has a parent pointer.

Note: This problem is a premium LeetCode problem. The key difference from #236
is that each node has a `parent` pointer. You do NOT have access to the root.

Hint: Think about a classic linked list problem...

Date: 2026-03-25
"""


class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def lowestCommonAncestor(p: Node, q: Node) -> Node:
    a, b = p, q
    while a != b:
        a = a.parent if a.parent else q
        b = b.parent if b.parent else p
    return a

# ─────────────────────────────────────────────
# 工具函数：方便测试
# ─────────────────────────────────────────────

def build_tree_with_parent(vals):
    """按层序构建带 parent 指针的二叉树"""
    if not vals:
        return None
    root = Node(vals[0])
    queue = [root]
    i = 1
    while queue and i < len(vals):
        node = queue.pop(0)
        if i < len(vals) and vals[i] is not None:
            node.left = Node(vals[i])
            node.left.parent = node
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = Node(vals[i])
            node.right.parent = node
            queue.append(node.right)
        i += 1
    return root


def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5),
        ([1, 2], 1, 2, 1),
    ]

    for tree_vals, p_val, q_val, expected_val in test_cases:
        root = build_tree_with_parent(tree_vals)
        p = find_node(root, p_val)
        q = find_node(root, q_val)
        result = lowestCommonAncestor(p, q)
        result_val = result.val if result else None
        status = "✓" if result_val == expected_val else "✗"
        print(f"{status} p={p_val}, q={q_val}")
        print(f"   Output:   {result_val}")
        print(f"   Expected: {expected_val}\n")

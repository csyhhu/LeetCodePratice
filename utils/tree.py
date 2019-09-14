"""
This code provides some helper function for tree
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTreePreOrderInOrder(preorder, inorder):
    """
    This function build a binary tree using preorder and inorder,
    but only in situation that elements are unique.
    :param preorder:
    :param inorder:
    :return:
    """
    if len(inorder) == 0 or len(preorder) == 0:
        return None

    root = TreeNode(preorder[0])
    root_in_idx = inorder.index(preorder[0])
    preorder.pop(0)
    root.left = buildTreePreOrderInOrder(preorder, inorder[: root_in_idx])
    root.right = buildTreePreOrderInOrder(preorder, inorder[root_in_idx + 1:])

    return root


def buildTreeWithLevelInfo(info):
    """
    :param info: [-0, --1, --0, ---0, ---1]
    :return:
    """
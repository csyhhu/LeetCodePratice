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
    pass


def buildTreeWithOrder(nums, index):
    """
    Build a tree given the nums, such as: [5,3,6,2,4,null,null,1]. 2 * i+1 and 2 * i+2 is the left/right child of i
    :param nums:
    :return:
    """
    if nums[index] == 'null':
        return

    root = TreeNode(nums[index])

    if 2 * index + 1 < len(nums):
        root.left = buildTreeWithOrder(nums, 2 * index + 1)
    if 2 * index + 2 < len(nums):
        root.right = buildTreeWithOrder(nums, 2 * index + 2)

    return root


def InOrderTraverse(root, path = []):
    """
    :param root:
    :param path:  An empty placeholder
    :return:
    """
    if root is not None:
        if root.left is not None:
            path = InOrderTraverse(root.left, path)
        path.append(root.val)
        if root.right is not None:
            path = InOrderTraverse(root.right, path)
    return path


if __name__ == '__main__':

    from utils.printResults import printTreePreorder

    inputs = [5,3,6,2,4,'null','null',1]
    root = buildTreeWithOrder(inputs, 0)
    printTreePreorder(root)

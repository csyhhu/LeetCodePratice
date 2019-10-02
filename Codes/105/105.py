from utils.printResults import printTreePreorder

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder, inorder):

    if len(inorder) == 0 or len(preorder) == 0:
        return None

    root = TreeNode(preorder[0])
    root_in_idx = inorder.index(preorder[0])
    preorder.pop(0)
    root.left = buildTree(preorder, inorder[: root_in_idx])
    root.right = buildTree(preorder, inorder[root_in_idx + 1:])

    return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = buildTree(preorder, inorder)
path = printTreePreorder(root)
print(path)
from utils.printResults import printTreePreorder
from utils.tree import TreeNode, buildTreePreOrderInOrder

def pruneTree(root):

    def containsOne(node):

        if node is None:
            return False

        left_contains_1 = containsOne(node.left)
        right_contains_1 = containsOne(node.right)

        if not left_contains_1:
            node.left = None
        if not right_contains_1:
            node.right = None

        return node.val == 1 or left_contains_1 or right_contains_1

    containsOne(root)
    return root
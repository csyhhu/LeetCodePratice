class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def printTreePreorder(cur_node):

    if cur_node is None:
        print('NULL')
        return

    print(cur_node.val)
    printTreePreorder(cur_node.left)
    printTreePreorder(cur_node.right)

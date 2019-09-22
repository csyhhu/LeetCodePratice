class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def printTreePreorder(cur_node, path=[]):

    if cur_node is None:
        # print('NULL')
        path.append('NULL')
        return

    # print(cur_node.val)
    path.append(cur_node.val)
    printTreePreorder(cur_node.left, path)
    printTreePreorder(cur_node.right, path)

    # print(path)
    return path

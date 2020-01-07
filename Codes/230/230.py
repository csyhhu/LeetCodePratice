from utils.tree import buildTreeWithOrder

def kthSmallest_recursive(root, k):

    order = []

    def InOrderTraverse(root, order):
        if root is not None:
            if root.left is not None:
                order = InOrderTraverse(root.left, order)
            order.append(root.val)
            # if len(order) == k:
            #     return order
            if root.right is not None:
                order = InOrderTraverse(root.right, order)
        return order

    InOrderTraverse(root, order)
    return order[k-1]


def kthSmallest_iterative(root, k):

    stack = []
    while True:
        # Step 1: All the way down to the bottom
        while root:
            stack.append(root)
            root = root.left
        # Step 2: Pop up
        root = stack.pop()
        k -= 1
        if k== 0:
            return root.val
        # Step 3: Change to the right
        root = root.right


# inputs = [3,1,4,'null',2]
# k = 1
inputs = [5,3,6,2,4,'null','null',1]
k = 3
root = buildTreeWithOrder(inputs, 0)
# print(kthSmallest_iterative(root, k))
# print(kthSmallest_recursive(root, k))
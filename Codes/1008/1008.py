# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

def bstFromPreorder(self, preorder):
	"""
	Construct a BST from the given preorder list, which means we don't need to explicitly construct the BST,
	rather just reconstruct a tree given this preorder, but also need to consider the property of BST.

	It seems not so difficult but why I think it is difficult?
	"""
	root = TreeNode(preorder[0])

	def construct_BST(node, val):

		if node is None:
			return

		if val < node.val:
			if node.left is None:
				node.left = TreeNode(val)
			else:
				construct_BST(node.left, val)

		if val > node.val:
			if node.right is None:
				node.right = TreeNode(val)
			else:
				construct_BST(node.right, val)


	for val in preorder[1:]:
		construct_BST(root, val)
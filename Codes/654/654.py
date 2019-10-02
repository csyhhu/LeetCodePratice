# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def traverse(root, path=''):
    
    # if root is None:
    #     # print ('NULL')
    #     path += 'null '
    #     return
    # else:
    #     path += (str(root.val) + (' '))
    #     # path += str(root.val)
    #     # print(root.val)
    # path = traverse(root.left, path)
    # path = traverse(root.right, path)
    
    # return path

    if root is None:
        print ('NULL')
        return
    else:
        print(root.val)
    traverse(root.left, path)
    traverse(root.right, path)

class Solution(object):
    
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def constructTree(nums):
            
            if len(nums) == 0:
                root = None
                return
            
            root = TreeNode(max(nums))
            split_idx = nums.index(max(nums))
            # print(nums[split_idx + 1: ])
            root.right = constructTree(nums[split_idx + 1: ])
            root.left = constructTree(nums[0: split_idx])
            return root

        root = constructTree(nums)
        return root

s = Solution()
mbt = s.constructMaximumBinaryTree([3,2,1,6,0,5])
print (traverse(mbt))
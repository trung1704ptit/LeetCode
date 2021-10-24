"""
This problem can be solved by DFS (Depth first search)
If root has left and right:
- we will calculate number of node left and right, 
- get min of them

if root has only left or right:
- because of only left and right,
- so we will find depth of left or right, get max of them

Plus with 1: because 1 is root
"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
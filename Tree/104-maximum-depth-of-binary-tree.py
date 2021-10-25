# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        if root.left == None and root.right == None:
            return 1
        
        # root has only right subtree:
        if not root.left:
            return 1 + self.maxDepth(root.right)
        
        # root has only left subtree:
        if not root.right:
            return 1 + self.maxDepth(root.left)
        
        # if none of the above cases
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
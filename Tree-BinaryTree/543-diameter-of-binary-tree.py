"""
For each node, find the max subtree depth (left, right)
using a variable res, res will be update or each recursion.
"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    res = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if root is None:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)
            
            self.res = max(self.res, r + l)
            return max(l, r) + 1

        if root is None:
            return 0
        
        dfs(root)
        
        return self.res
        
        
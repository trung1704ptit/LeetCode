# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
            
    res = 0
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """    
        def dfs(node, isLeft):
            if node is None:
                return
            if node.left is None and node.right is None:
                if isLeft:
                    self.res += node.val
                return
            dfs(node.left, True)
            dfs(node.right, False)
        
        dfs(root, None)
        
        return self.res
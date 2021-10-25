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
        
        self.res = 0
        self.__traversal(root)
        
        return self.res
    
    def __traversal(self, node):
        if not node:
            return

        if node.left and not node.left.left and not node.left.right:
            self.res += node.left.val

        self.__traversal(node.left)
        self.__traversal(node.right)

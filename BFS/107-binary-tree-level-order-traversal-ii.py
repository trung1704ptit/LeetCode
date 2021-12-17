"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = []
        visited =set()
        q.append(root)
        res = []
        
        if root is None:
            return res
        
        while q:
            current_level = []
            current_size = len(q)
            for i in range(current_size):
                u = q.pop(0)
                if u is not None:
                    current_level.append(u.val)
                    if u.left:
                        q.append(u.left)
                    if u.right:
                        q.append(u.right)
            res.append(current_level)
            
        return res[::-1]
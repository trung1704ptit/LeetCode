"""
https://leetcode.com/problems/n-ary-tree-level-order-traversal/
"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
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
                    for v in u.children:
                        q.append(v)
            res.append(current_level)
            
        return res
            
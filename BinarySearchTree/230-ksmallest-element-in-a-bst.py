"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Solution:
We use a array to get the value of the node,
return element [k-1] is k-smallest
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):     
        self.nodes = []

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.solve(root)
        return self.nodes[k-1]
    
    # nodes is the nodes that we processed
    def solve(self, root):
        if root is None:
            return
        
        self.solve(root.left)
        self.nodes.append(root.val)
        self.solve(root.right)
        
        
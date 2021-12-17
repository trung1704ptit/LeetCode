# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        q = []
        res = []
        if root is None:
            return res
        
        q.append(root)
        
        while q:
            len_queue = len(q)
            for i in range(len_queue):           
                u = q.pop(0)
                if u.left:
                    q.append(u.left)
                if u.right:
                    q.append(u.right)

            res.append(u.val)
                
        return res
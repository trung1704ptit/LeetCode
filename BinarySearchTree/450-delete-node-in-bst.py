# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minValueNode(self, node):
        current = node
        # loop down to find the left most leaf
        while(current.left is not None):
            current = current.left
        return current
        
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            else:
                # Node with two children:
                # Get the inorder successor
                # (smallest in the right subtree)
                
                temp = self.minValueNode(root.right)
                # Copy the value of inorder-successor to the node
                root.val = temp.val
                
                root.right = self.deleteNode(root.right, temp.val)
                
        return root
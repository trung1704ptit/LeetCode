"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Using two pointers

- Initialize two pointers slow and fast, pointing to the head of the linked list.
- Move fast pointer n steps ahead.
- Now, move both slow and fast one step at a time unless fast reaches to the end. The fast pointer will definitely reach to the end before slow because it is ahead.
- When we fast pointer reaches to the end, the slow pointer will be n steps behind it i.e., n steps behind the end of the list.
- At that point, we will remove the node and link it to the next of current node.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        # using two pointers         
        slow =  head
        fast =  head
        
        # move fast to the nth of list first         
        for i in range(0, n):
            # if n is equal the number of nodes
            if fast.next is None:
                if i == n - 1:
                    head = head.next
                return head
            
            fast = fast.next
        
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
            
        # now fast is end of list, slow in nth position
        if slow.next is not None:
            slow.next = slow.next.next
            
        return head
            
"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# time complexity: O(m+n) with m, n are the numbers of node of list1 and list2
# space: O(1): we only using temp, head, but we just maintain the next property


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = []

        # basecase
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        # choose head which is smaller of two lists
        if list1.val < list2.val:
            temp = head = ListNode(list1.val)
            list1 = list1.next
        else:
            temp = head = ListNode(list2.val)
            list2 = list2.next
            
        # Loop until any of the list becomes null
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                temp.next = ListNode(list1.val)
                list1 = list1.next
            else:
                temp.next = ListNode(list2.val)
                list2 = list2.next
                
            temp = temp.next
            
        # add all the nodes in list1, if remaining
        while list1 is not None:
            temp.next = ListNode(list1.val)
            list1 = list1.next
            temp = temp.next
            
        # add all the nodes is list2, if remaining
        while list2 is not None:
            temp.next = ListNode(list2.val)
            list2 = list2.next
            temp = temp.next
      
        return head

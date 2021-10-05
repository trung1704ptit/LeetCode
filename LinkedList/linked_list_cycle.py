# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dic = {}
        i = 0
        curr = head
        while curr != None:
            if curr not in dic:
                dic[curr] = i
                i += 1
                curr = curr.next
            else:
                return curr
        return None
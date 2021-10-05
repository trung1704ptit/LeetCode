class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        next = None
        while head:
            head.next, head, next = next, head.next, head
        return next
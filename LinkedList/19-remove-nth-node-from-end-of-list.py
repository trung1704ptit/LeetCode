"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Using two pointers

- Initialize two pointers slow and fast, pointing to the head of the linked list.
- Move fast pointer n steps ahead.
- Now, move both slow and fast one step at a time unless fast reaches to the end. The fast pointer will definitely reach to the end before slow because it is ahead.
- When we fast pointer reaches to the end, the slow pointer will be n steps behind it i.e., n steps behind the end of the list.
- At that point, we will remove the node and link it to the next of current node.
"""


"""
https://leetcode.com/problems/kth-largest-element-in-an-array
Solution:
Using min-heap
build and min-heap from 0->k of list
loop k => size
if current element > root, relace root with current element,
else continue
return the root of min-heap
"""
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        # base case
        if not nums or len(nums) < k:
            exit(-1)
        
        # build min-heap with nums of nodes: k nodes
        pq = nums[0:k]
        heapq.heapify(pq)

        # do for the remaining list elements
        for i in range(k, len(nums)):
            # if the current element greater than root of heap:
            if nums[i] > hq[0]:
                # pop the smallest item and push the new item into heap, heap size doesn't change.
                heapq.heapreplace(pq, nums[i])

        # return the root of heap, that is the k largest element
        return pq[0]


# Time complexity:  O(n.log(k))
        
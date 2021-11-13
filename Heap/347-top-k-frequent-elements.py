"""
https://leetcode.com/problems/top-k-frequent-elements/
Solution:
Using Max-Heap
- Using Counter lib to count the frequent of each element in array
- using max-heap to push counts to heap
- Pop k times to get the k nodes => result.
"""

import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        counts = Counter(nums)
        max_heap = []
        for key, val in counts.items():
            # Heap elements can be tuples. This is useful for assigning comparison values.
            # Using "-val" becasue we will using heappop (get the smallest element in heap)
            # So we will push the larger element to the end of tree of heap.
            heapq.heappush(max_heap, (-val, key))
        result = []
        
        while k > 0:
            # apppend the freequent number of element (the key of each node)
            result.append(heapq.heappop(max_heap)[1])
            k -= 1
            
        return result
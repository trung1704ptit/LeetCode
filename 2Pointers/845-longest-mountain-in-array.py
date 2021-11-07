"""
Solution:
Using 2 pointers
slow and fast
using res to count the length of mountain.
"""


class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        s = 0
        while s < len(arr):
            f = s
            while f + 1 < len(arr) and arr[f] < arr[f+1]:
                f += 1
            # m is mountain
            m = f
            while m + 1 < len(arr) and arr[m] > arr[m+1]:
                m += 1
            
            if f != m and s != f:
                res = max(res, m-s+1)
            
            if s != m:
                s = m
            else:
                s += 1
                
        return res
            
        
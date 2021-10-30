"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/

- Is array always has an mountain?

***************************************************

Using Binary search
We will find middle of array, imagine have 2 parts
Using Lo, Hi, Mid variables
If middle in left part, set low is middle
If middle in right part, set Hi is middle
Loop until we get the value of mid is more than left and mode than right.
"""


class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """ 
        lo = 0
        hi = len(arr) -1
        
        while lo <= hi:
            mid = lo + (hi-lo)/2
            if mid > 0 and mid < len(arr)-1 and arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            
            if mid == 0 or arr[mid] > arr[mid-1]:
                lo = mid + 1
            elif mid == len(arr)-1 or arr[mid] > arr[mid+1]:
                hi = mid - 1
                
        return -1
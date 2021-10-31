"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Solution:
- Using binary search
- Find the rotated point.
- the min value is next to the right of rotated point.

Using binary search to find the rotated point
if nums[mid] > nums[mid +1] and mid +1 < len(nums):
    => rotated point = mid
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(nums) -1
        rotated_point = -1
        
        while left <= right:
            mid = left + (right - left)/2
            
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                rotated_point = mid
                break
            
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
                
        return nums[rotated_point + 1]
        
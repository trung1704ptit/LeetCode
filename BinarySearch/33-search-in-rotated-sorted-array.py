"""
https://leetcode.com/problems/search-in-rotated-sorted-array

Solution:
[4,5,6,7,0,1,2]      
Exam:
Find the 7  will greater all the element to the right => we will search target in two parts, seperated by num 7
- Find the index of the smallest element
- Now we will have 2 part, check target belong part1 or part2
- Binary search to find the index of target in array
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if nums == None or len(nums) == 0:
            return -1
        
        # Find the index of smallest element, assign it to low variable
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) / 2
            # check if the middle is greater all the right
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        # after while, the low will be the smallest element in the array
        # Now we will have 2 part, check target belong part1 or part2
        # Binary search to find the index of target in array

        start = low
        low = 0
        high = len(nums) - 1

        # we need to know we will search in part1 or part2
        if target >= nums[start] and target <= nums[high]:
            low = start
        else:
            high = start

        while low <= high:
            mid = low + (high-low) /2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1

        return -1
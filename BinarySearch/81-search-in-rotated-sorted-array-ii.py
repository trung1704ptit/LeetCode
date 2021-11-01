"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii

When nums [mid] = nums [left], at this time, because it is difficult to determine where the target will fall, then only left ++
When nums [mid]> nums [left], it can be divided into two cases at this time, it is relatively simple to judge the left half
When nums [mid] <nums [left], it can be divided into two cases at this time, it is relatively simple to judge the right half
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        left, right = 0, len(nums) -1
        while left <= right:
            mid = left + (right - left)/2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[left]:
                left +=1
            elif nums[mid] > nums[left]:
                # two case:
                if nums[mid] > target and nums[left] <= target:
                    # target maybe now in left of mid
                    right = mid - 1
                else:
                    # target maybe now in right of mid
                    left =  mid + 1
            else:
                # two case
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
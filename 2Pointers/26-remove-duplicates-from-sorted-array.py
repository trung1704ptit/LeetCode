"""
Solution:
- start with index = 1
- Using w start with 1 as the new index of nums
- Loop to array, compare if the current value not equal to the prev value => set value to the nums
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        w = 1
        n = len(nums)
        if n == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[w] = nums[i]
                w += 1
        
        return w
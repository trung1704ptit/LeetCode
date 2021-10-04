class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        boundary = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[i], nums[boundary] = nums[boundary], nums[i]
                boundary +=1
                
        return nums
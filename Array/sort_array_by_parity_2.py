class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        i = 0
        j = 1

        while i < len(nums) and j < len(nums):
            if nums[i] % 2 != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 2
            else:
                i += 2

        return nums

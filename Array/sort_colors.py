class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        """
        Start with element number 2 (index = 1)
        We imagine that we have 2 list, sorted list and unsorted list
        Compare the key with the last element of sorted list
        """
        # Insertion sort
        for i in range(1, len(nums)):
            key = nums[i]

            j = i - 1

            while j >= 0 and key < nums[j]:
                nums[j+1] = nums[j]
                j -= 1

            nums[j+1] = key

        return nums

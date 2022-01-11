class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = -1
        last = -1
        n = len(nums)
        for i in range(0, n):
            if target != nums[i]:
                continue
            if first == -1:
                first = i
            last = i
            
        return [first, last]
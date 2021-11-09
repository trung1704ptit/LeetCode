"""
"""

class Solution(object):
    def threeSumSmaller(self, nums, k):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        n = len(nums)
        count = 0
        for i in range(0, n-2):
            low = i + 1
            high = n - 1
            while low < high:
                if nums[i] + nums[low] + nums[high] < k:
                    count += high - low
                    low += 1
                else:
                    high -= 1

        return count
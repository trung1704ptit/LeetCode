"""
https://leetcode.com/problems/house-robber/
Maximum amount of money => think to DP
- Decided rob this house will be effected to choose the next house

Framework:
- Defination: f[i] the maximum money when the last house is ith
- Relation: f[i] = max(nums[i] + f[i-2], f[n-1])
- Basecase: f[0] = nums[0]; f[1] = max(nums[0], nums[1])
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        
        f = [x for x in range(n)]
        f[0] = nums[0]
        f[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            f[i] = max(nums[i] + f[i-2], f[i-1])
            
        return f[n-1]
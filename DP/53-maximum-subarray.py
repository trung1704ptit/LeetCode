"""
https://leetcode.com/problems/maximum-subarray/
"""

"""
----------------------------------------------------------
Solution 1
Using one loop
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) < 0:
            return max(nums)
        
        curr_sum, max_sum = 0, 0
        for num in nums:
            curr_sum = max(0, curr_sum + num)
            max_sum = max(curr_sum, max_sum)
            
        return max_sum
                





"""
----------------------------------------------------------
Solution 2
Dynamic programming
dp[i] is the maximum 
"""

class Solution(object):
    def maxSubArray(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            if dp[i] > max_sum:
                max_num = dp[i]

        return max_num
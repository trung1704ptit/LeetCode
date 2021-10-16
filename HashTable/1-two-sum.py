"""
https://leetcode.com/problems/two-sum/      

Questions:
- 

Solutions:
- Using Hashtable to store the number as key and index as value
- Compare the target - current_num is in dict => True

Example:
nums = [2,7,11,15], target = 9

dict = {}
el nums[0] = 2: 9 - 2 = 7 not in dict => add 2 to dict, dict[2] = 0
el nums[1] = 7: 9 - 7 = 2 in dict => return True

"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        
        for i, n in enumerate(nums):
            if target - n in d:
                return [d[target - n], i]
            d[n] = i
            
        return False
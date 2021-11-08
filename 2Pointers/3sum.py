"""
Solution:
- using two poiners
+ sort the array, (in time O (n * logn))
+ loop for each i, following steps:
+ pointer left: j = i + 1, pointer right: k = len(nums) - 1
+ check if sum i, j, k === 0 => return subarray
 -- if sum i, j, k > 0 => decrease k by 1
 -- if sum i, j, k < 0 => increase j by 1

 To avoid duplicate i, check i and i - 1, if nums[i] == nums[i-1] => continue
 To avoid duplicate j, check j and j - 1, if nums[j] == nums[j-1] => j +=1
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        n = len(nums)
        
        
        for i in range(0, len(nums)):
            # avoid duplicate for i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = n - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # avoid duplicate for j
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    
        return res
                    
        
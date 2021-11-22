"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/
"""

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        resultdict = {}
        for i in nums:
            if resultdict.has_key(i):
                resultdict[i] += 1
            else:
                resultdict[i] = 1
        
        ans = []
        for i in resultdict:
            if (resultdict[i] == 2):
                ans.append(i)
                
        return ans
"""
https://leetcode.com/problems/contains-duplicate/

Solution:
[1,2,3,1]
Using Hashtable - in python call dictionary
Store key and value in dict
We will loop through the array and add key and value into dict
example:
dict = {}
dict[1] = 1
dict[2] = 2
dict[3] = 3
dict[1] => exits on dict => return True
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        my_dict = {}
        
        for n in nums:
            if n in my_dict:
                return True
            else:
                my_dict[n] = n
        
        return False
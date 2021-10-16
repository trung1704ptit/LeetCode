"""
https://leetcode.com/problems/contains-duplicate-ii/

Question:
- How about if array includes more than 2 element with the same value?

Solutions:
- Using Hashtable
- Store the value of element as the key in dict, store the index of array as value of dict
- Check if value exist on hash, will compare the distance of index

Example:
nums = [1,2,3,1], k = 3

dict = {}
for array ...
dict[1] = 0 (1 is not in dict => add to dict)
dict[2] = 1 (2 is not in dict => add to dict)
dict[3] = 2 (3 is not in dict => add to dict)
dict[1] = 3 (1 is in dict => compare the distance of index, current_index = 3 and the last index is 0)

distance = 3 - 0 = 3 <= k = 3
=> return True
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        my_dict = {}
        for index, n in enumerate(nums):
            if n in my_dict and index - my_dict[n] <= k:
                return True
            my_dict[n] = index
                
        return False
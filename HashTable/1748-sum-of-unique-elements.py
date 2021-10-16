"""
https://leetcode.com/problems/sum-of-unique-elements/

Questions:
- Is the array include negative number?
- Is the array include float?

Solutions:
- Using a hashmap to store the counter of each number
- Find the element that has counter equal 1, sum this value
"""

class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        d = {}
        
        for i, n in enumerate(nums):
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        sum = 0
        for n in d:
            if d[n] == 1:
                sum += n
            
        return sum
            
            
# Time: O(n) because using 2 loop
# space: O(1)
"""
https://leetcode.com/problems/first-unique-character-in-a-string/

Questions:
- Is that string contains lowercase or upercase?
- Is that uinique if a and A appear in string?

Solutions:
- Using hashmap to store the number counter of each character
- if string count equal 1 => return index
"""

import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        print(count)
        
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
    
# Time: O(n) loop through string 2 time
# space: O(1) because the string is alphabet with 26 characters 
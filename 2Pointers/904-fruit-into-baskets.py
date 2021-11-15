"""
https://leetcode.com/problems/fruit-into-baskets/

Solution:
using two pointer, but first using a dict to store the number of each element.
- using j = 0 as a pointer,
- loop i from 0 -> n
increase the number of each element into dict,
check if len dict  > 2:
   + decrease the number of element j
   + check if number of element j is 0, remove it from dict
   + increase j += 1
compare result = max(result, i - j + 1)
"""

from collections import defaultdict

class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        
        n = len(fruits)
        j = 0
        result = 0
        d = defaultdict(int)
        
        for i, v in enumerate(fruits):
            d[v] += 1
            while len(d) > 2:
                d[fruits[j]] -= 1
                if d[fruits[j]] == 0:
                    del d[fruits[j]]
                j += 1

            result = max(result, i - j + 1)
        return result

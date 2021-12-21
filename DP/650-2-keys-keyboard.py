"""
https://leetcode.com/problems/2-keys-keyboard/
Using DP

"""


class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(2, n+1):
            while n % i == 0:
                res += i
                n /= i
        return res


"""
------------------------------------------------------------------------
"""
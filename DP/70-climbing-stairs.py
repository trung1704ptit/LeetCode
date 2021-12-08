"""
https://leetcode.com/problems/climbing-stairs/

Using DP because
- the way to climb to ith depends on the number way to climb to i-1
* framework:
- difinition: f[i] is the number of way to climb to ith
- relation: f[i] = f[i-1] + f[i-2]
- base case: f[0] = 1; f[1] = 2
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = []
        
        f.append(1)
        f.append(2)
        
        for i in range(2,n):
            f.append(f[i-2] + f[i-1])
            
        return f[n-1]
        
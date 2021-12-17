"""
https://leetcode.com/problems/unique-paths/
"""

"""
Using Dynamic programming
- number way to grid[i][j] is depends on number of way to [i-1] and [j-1]
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        res = 0
        dp = [[0] * (n) for i in range(m)]
        for i in range(m):
            dp[i][0] = 1

        for j in range(n):
            dp[0][j] = 1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
        
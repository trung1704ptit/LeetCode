"""
https://leetcode.com/problems/minimum-path-sum

Using Dynamic programming
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        dp = [[0 for j in range(0, n)] for i in range(0, m)]

        dp[0][0] = grid[0][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
            
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
        
                
        return dp[m - 1][n - 1]
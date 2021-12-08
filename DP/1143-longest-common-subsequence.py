"""
https://leetcode.com/problems/longest-common-subsequence/
Using DP
The comparation of i,j is depends on the the i-1 and j-1

call 2 text is s, t
s[i] == t[i] => f[i][j] = f[i-1][j-1]
s[i] != t[i] => f[i][j] = max(f[i-1][j], f[i][j-1])
"""

from collections import defaultdict

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n = len(text1)
        m = len(text2)
        if m*n == 0: return 0
        

        # [
        #     [0 0 0]
        #     [0 0 0]
        #     [0 0 0]
        # ]
        fx = [[0] * (m+1) for i in range((n+1))]
            
        for i in range(1, n+1):
            for j in range(1, m+1):
                fx[i][j] = max(fx[i-1][j], fx[i][j-1])
                
                if text1[i-1] == text2[j-1]:
                    fx[i][j] = max(fx[i][j], fx[i-1][j-1] + 1)
                    
        return fx[n][m]

"""
https://leetcode.com/problems/delete-operation-for-two-strings/
Using DP
- This problem siminal to longest common subsequence.
The number of way to remove charecter is depends on the previous way.


Minimum number steps required to make word1 and word2 the same:
- find the longest common subsequence
- if word1 and word2 have no common string => the steps is m+n
- if word1 and word 2 have lcs common character => the steps = m + n - 2*lcs
"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return len(word1) + len(word2) - 2 * self.lcs(word1, word2)
 
    def lcs(self, word1, word2):
        len1, len2 = len(word1), len(word2)
        dp = [[0] * (len2 + 1) for x in range(len1 + 1)]
        for x in range(len1):
            for y in range(len2):
                dp[x + 1][y + 1] = max(dp[x][y + 1], dp[x + 1][y])
                if word1[x] == word2[y]:
                    dp[x + 1][y + 1] = dp[x][y] + 1
        return dp[len1][len2]
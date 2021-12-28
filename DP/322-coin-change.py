"""
https://leetcode.com/problems/coin-change/
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # DP[i] is number of coin that amount i.
        # DP[i] = min(DP[i], DP[i- coins[i]] + 1)
        
        if not coins or amount < 0:
            return 0
        
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
        
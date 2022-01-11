class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        if prices is None or len(prices) <= 1:
            return res
        
        min_val = prices[0]
        for p in prices:
            if p > min_val:
                res = max(res, p - min_val)
            else:
                min_val = p
                
        return res
class Solution(object):
    def subsets(self, nums):
        res = [[]]
        for n in nums:
            res += [[n]+r for r in res]
        return res
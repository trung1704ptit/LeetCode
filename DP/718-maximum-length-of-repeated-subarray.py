"""
https://leetcode.com/problems/maximum-length-of-repeated-subarray
"""

"""
Brute force
- Loop though all the elements in A and B, and check the corrensponding matchness
- if elements match, we check as far as we can and then get the maximum length
- else skip

time complexity O(mn^2)
space O(1)
"""


class Solution(object):
    def findLength(self, nums1, nums2):
        res = 0
        for i, n1 in enumerate(nums1):
            for j, n2 in enumerate(nums2):
                if n1 == n2:
                    k = 1
                    while i + k < len(nums1) and j + k < len(nums2) and nums1[i+k] == nums2[j+k]:
                        k += 1
                    res = max(res, k)
        return res
                    



"""
Dynamic programming

"""

class Solution(object):
    def findLength(self, nums1, nums2):
        res = 0
        m =len(nums1)
        n = len(nums2)
        dp = [[0]*(n+1) for i in range(m +1)]

        for i, n1 in enumerate(nums1):
            for j, n2 in enumerate(nums2):
                if n1 == n2:
                    dp[i+1][j+1] = dp[i][j] + 1
                    res = max(res, dp[i+1][j+1])
        return res
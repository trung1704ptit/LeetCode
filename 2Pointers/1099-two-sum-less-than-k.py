"""
Solution:
- Using two pointer
- We need to sort array first.

left pointer start from 0
right pointer start from len(nums) - 1
res = -1
using a while loop, check sum = nums[l] + nums[r]:
- if sum > k:
    r -= 1
- if sum < k:
    l += 1
    res = max(res, sum)
"""


class Solution {
    def twoSumLessThanK(self, nums, k):
        i = 0
        j = len(nums) - 1
        res = -1
        while i < j:
            s = nums[i] + nums[j]
            if s >= k:
                j -= 1
            else:
                i += 1
                res = max(res, s)

        return res
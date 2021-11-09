"""
Solution:
- Using two pointer:
Loop to all element of array,
using low, high pointer,
"""

# Time:  O(n^2)
# Space: O(1)
class Solution:
    def threeSumSmaller(self, nums, target):
        nums.sort()
        n = len(nums)
 
        count, i = 0, 2
        # i start from 2, beacause we have at least 3 element.
        while i < n:
            l, r = 0, i - 1
            while l < r:  # Two Pointers, linear time.
                if nums[i] + nums[l] + nums[r] >= target:
                    r -= 1
                else:
                    count += r - l
                    l += 1
            i += 1
 
        return count　　


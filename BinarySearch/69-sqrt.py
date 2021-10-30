"""
Solution:
- Using binary search
- using lo, hi, mid
find the middle,
if middle * middle == x => return middle
Loop until find the mid * mid == x, or
if mid * mid > x, set lo = mid,
if mid * mid < x, set hi = mid
After loop, we have lo, have, mid,
check if hi * hi == x => return hi,
else return lo // because now: lo * lo < x, and hi * hi > x
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        lo = 0
        hi = x
        
        while lo + 1 < hi:
            mid = lo + (hi-lo)/2
            
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                lo = mid
            else:
                hi = mid
                
        if hi * hi == x:
            return hi
        
        return lo
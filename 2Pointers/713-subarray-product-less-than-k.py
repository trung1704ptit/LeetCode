class Solution(object):
    def numSubarrayProductLessThanK(self, array, k):
        """
        :type array: List[int]
        :type k: int
        :rtype: int
        """
        n = len(array)
        count = 0
        for i in range(0, n):

            # Counter for single element
            if array[i] < k:
                count += 1

            mul = array[i]

            for j in range(i + 1, n):

                # Multiple subarray
                mul = mul * array[j]

                # If this multiple is less
                # than k, then increment
                if mul < k:
                    count += 1
                else:
                    break
        return count



# ----------------------------------------------------


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        
        prod = 1
        count = 0
        left = 0
        for right, n in enumerate(nums):
            prod *= nums[right]
            while prod >= k:
                prod = prod // nums[left]
                left +=1

            count += right - left + 1
            
        return count
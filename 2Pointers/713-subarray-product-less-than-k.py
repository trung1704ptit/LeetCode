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
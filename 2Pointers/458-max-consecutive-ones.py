"""
Bruteforce solution:
using counter, loop for each element in array, if element is 1, counter++
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # intitialize count
        count = 0

        # initialize max
        result = 0

        for i in range(0, n):
            # Reset count when 0 is found
            if (nums[i] == 0):
                count = 0

            # If 1 is found, increment count
            # and update result if count
            # becomes more.
            else:

                # increase count
                count+= 1
                result = max(result, count)

        return result


"""
Using 2 pointers:
Using two pointer fast and slow

"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast, glo_max, loc_max = 0, 0, 0, 0
        while fast < len(nums):
            if nums[fast] == 0:
                loc_max = fast - slow  
                glo_max = max(glo_max, loc_max)
                slow = fast + 1      # need to add one more because we haven't incremented fast yet

            fast += 1
        loc_max = fast - slow        # end check for cases that end with 1
        return max(loc_max, glo_max)
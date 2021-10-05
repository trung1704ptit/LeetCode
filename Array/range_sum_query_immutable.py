class NumArray(object):
    def __init__(self, nums):
        self.sums = nums[:]

        for i in range(1, len(self.sums)):
            self.sums[i] = self.sums[i-1] + nums[i]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sums[j]
        return self.sums[j] - self.sums[i-1]


# sum[ i ] can be viewed as sum[ 0 to i ]
# sum[ j ] can be viewed as sum[ 0 to j ]
# sum[ i-1 ] + sum[ i to j ] = s[ 0 to j ]
# sum [ i to j ] = sum[ j ] - sum[ i-1 ]

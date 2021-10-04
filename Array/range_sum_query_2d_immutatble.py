class NumMatrix(object):

    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            return None

        row = len(matrix)
        col = len(matrix[0])
        self.sums = [[0]*(col+1) for _ in range(row+1)]
        for i in range(1, row+1):
            for j in range(1, col+1):
                self.sums[i][j] = self.sums[i][j-1]+self.sums[i -
                                                              1][j]-self.sums[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        return self.sums[row2+1][col2+1] - self.sums[row2+1][col1] - self.sums[row1][col2+1] + self.sums[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

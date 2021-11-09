class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        
        r = 0
        c = cols - 1
        
        while True:
            if r < rows and c >= 0:
                if matrix[r][c] == target:
                    return True
                elif matrix[r][c] > target:
                    c -= 1
                else:
                    r += 1
            else:
                return False
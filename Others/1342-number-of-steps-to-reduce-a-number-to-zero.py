"""

"""


"""
Solution1:
Using a while:
"""
class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        counter = 0
        while num != 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num -= 1
            counter +=1
        return counter
            
    
"""

"""
class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sum = 0
        hash_map = {}
        hash_map[0] = 1   
        for n in nums:
            sum += n
            modulo = sum % k
            if modulo in hash_map:
                count += hash_map[modulo]
            hash_map[modulo] = hash_map.get(modulo, 0) + 1
        
        return count
    
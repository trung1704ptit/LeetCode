"""
https://leetcode.com/problems/4sum-ii/

Questions:
-

Solutions:
Array A, B, C, D
- Using Hashmap
- for i in A
    for j in B
        if i + j not in hashmap => dict[i+j] = 1
        else:
            dict[i+j] += 1

- counter
for i in C:
    for j in D:
        if (-1) * (i+j) in dict:
            counter += dict[-1 * (i + j)]


Example:
nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
loop nums1 and loop nums2:
dict = {}
dict[1-2] = dict[-1] (- 1 not in dict) => d[-1] = 1
dict[1-1]= dict[0] (0 not in dict) => dict[0] = 1
dict[2-2] dict[0] (0 in dict) => dict[0] += 1 <=> dict[0] = 2
dict[2-1] = dict[1] (1 not in dict) => dict[1] = 1

loop nums3 and loop nums4:
dict[-1 * (-1 + 0)] = dict[1] (1 in dict) => counter += dict[1] = 1
dict[-1 * (-1 + 2)] = dict[-1] (-1 in dict) => counter += dict[-1] = 1 + 1 = 2
dict[-1 * (2 + 0)] = dict[-2] ( -2 not in dict)
dict[-1 * (2 + 2)] = dict[-4] (-4 not in dict)

return counter

"""

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        d = {}
        for i in nums1:
            for j in nums2:
                if i + j not in d:
                    d[i+j] = 1
                else:
                    d[i+j] +=1
                    
        counter = 0
        for i in nums3:
            for j in nums4:
                if (-1) * (i + j) in d:
                    counter += d[-1 * (i+j)]
                    
        
        return counter
                
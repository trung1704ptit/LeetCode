"""
https://leetcode.com/problems/find-anagram-mappings/

Solutions 1:
- loop through A

- using a array to store the index of element A in B

"""

# Solution 1, Using array
class Solution:
    def anagramMappings(self, A, B):
        results = []
        for number in A:
            results.append(B.index(number))

        return number


# Solution 2 using HashMap
class Solution:
    def anagramMappings(self, A, B):
        d = {}
        for i, number in enumerate(B):
            d[number] = i

        return [d[val] for val in A]
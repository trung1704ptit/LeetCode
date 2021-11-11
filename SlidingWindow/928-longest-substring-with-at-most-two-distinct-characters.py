"""
Solution:

"""
from collections import Counter

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter()
        
        left, max_length = 0, 0
        for right, char in enumerate(s):
            counter[char] += 1
            while len(counter) > 2:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            max_length = max(max_length, right-left+1)
        return max_length


"""
EX:
input: "eceba"
output:

- e
counter[e] = 1
max = max(0, 0 - 0 + 1) = 1

- c
counter[e] = 1
counter[c] = 1
max = max(1, 1-0 + 1)= 2

- e
counter[e] = 2
counter[c] = 1
max = max(2, 2-0 +1) = 3

- b
counter[e] = 2
counter[c] = 1
counter[b] = 1
len(counter) > 2 => counter[e] -= 1 => counter[e] = 1
left += 1 => "eceba"
               L
               


"""


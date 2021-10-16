"""
https://leetcode.com/problems/palindrome-permutation/

Questions:
- How about the string with upercase and lowercase, ex: abA ?

Solutions:
- If a string is palindrome, it should contain characters with even number of occurences
and one character with odd number of occurences, or only one character with even number of occurrences.

- Using Hastable to store the character
- if character already exist in hashtable => remove this character from hashtable
- loop to the end, if hashtable has length <= 1 => return palindrome

Example:
s = "aab"

dict = {}
s[0] = "a" not in dict => dict[a] = 1
s[1] = "a" in dict => remove "a" from dict
s[2] = "b" not in dict => dict[b] = 2

now length of dict = 1 <= 1 => return True
"""

class Solution(object):
    def canPermutePalindrome(self, s):
        odd_dict = {}
        for c in s:
            if c in odd_dict:
                del odd_dict[c]
            else:
                odd_dict[c] = c

        return len(odd_dict) <= 1

test = Solution()
result = test.canPermutePalindrome('carerac')
print(result)

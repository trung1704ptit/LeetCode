"""
https://leetcode.com/problems/word-break

Using BFS
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDictSet = set(wordDict)
        q = []
        q.append(0)
        seen=set()
        
        while q:
            start = q.pop(0)
            if start == len(s): return True
            if start in seen: continue
                
            print(seen)
            
            for end in range(start+1, len(s) + 1):
                print(s[start:end])
                if s[start:end] in wordDictSet:
                    q.append(end)
            
            seen.add(start)
            
        print(seen)
            
        return False

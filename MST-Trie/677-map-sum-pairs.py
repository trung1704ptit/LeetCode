"""
https://leetcode.com/problems/map-sum-pairs
Using Trie and Hashmap
- Trie: Storing prefix information
- Hashmap: Storing the value of each string
"""

class MapSum(object):

    def __init__(self):
        self.trie = Trie()
        self.dict = {}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        # check if key in dict, calculate the val, because we can add ["apple",3] serveral times
        # we need to update the new value to calculate for each char in insert method of Trie
        if key in self.dict:
            self.trie.insert(key, val - self.dict[key])
        # else if key is not in dict
        else:
            self.trie.insert(key, val)
        
        self.dict[key] = val
        
        
    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self.trie.search(prefix)


        

class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, val):
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
            current.val += val # set new val

    def search(self, prefix):
        current = self.root
        for c in prefix:
            current = current.children.get(c)
            if current is None:
                return 0

        return current.val
            

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
class Trie(object):

    def __init__(self):
        self.child = {}

        
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.child
        # for each letter l in word 
        for l in word:
            if l not in current:
                current[l] = {}
            current = current[l]
        current['#'] = 1
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current = self.child
        # for each letter l in word 
        for l in word:
            if l not in current:
                return False
            current = current[l]
        return '#' in current
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current = self.child
        # for each letter l in word 
        for l in prefix:
            if l not in current:
                return False
            current = current[l]
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
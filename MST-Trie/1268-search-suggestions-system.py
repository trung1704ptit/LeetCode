class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.child = {}
        self.top3 = []

class Trie(object):
    def __init__(self):
        self.root = TreeNode(None)

    def add(self,word):
        node = self.root

        for i in word:
            if i not in node.child:
                child_node = TreeNode(i)
                node.child[i] = child_node
            if len(node.top3) < 3:
                node.top3.append(word)
            node = node.child[i]

        if len(node.top3) < 3:
            node.top3.append(word)

    def search(self,prefix):
        node = self.root
        for i in prefix:
            if i not in node.child:
                return []
            node = node.child[i]
        return node.top3



class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        trie = Trie()
        for product in products:
            trie.add(product)
        res = []
        word = ''
        for char in searchWord:
            word += char
            res.append(trie.search(word))

        return res
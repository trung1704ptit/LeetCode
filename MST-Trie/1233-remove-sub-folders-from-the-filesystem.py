"""
https://leetcode.com/problems/remove-sub-folders-from-the-filesystem

"""


"""
Bruthforce first
- Sort the folders by len

["/a","/a/b","/c/d","/c/d/e","/c/f"]

after soft:
["/a","/a/b","/c/d","/c/f", "/c/d/e"]

Time complexcity:
    sort: nlog(n)
    loop: n*k with k is max length of folder
    ==> nlog(n) + n*k
Space: O(m) m is number of parents folder
"""

class Solution(object):
    def removeSubfolders(self, folder):
        # increasing by len
        folder.sort(key=lambda e:len(e))

        res = []

        for f in folder:
            flag = True

            for i in range(2, len(f)):
                if f[i] == '/' and f[:i] in res:
                    # that means f is the sub folder
                    flag = False
                    break
            if flag:
                res.append(f)

        return res




# --------------------------------------------------------------------------------------
"""
Using Trie
- Add all the folder into the trie
- loop for all f in folders
if char in f already exist in trie => not add to trie
else add to trie
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.childDir = {}
        self.isDir = False

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode(None)

    def insert(self,word):
        node = self.root
        for i in word:
            if i not in node.childDir:
                node.childDir[i] = TreeNode(i)
            node = node.childDir[i]
        node.isDir = True

    def isDelete(self,dir):
        node = self.root
        for i in dir:
            if i in node.childDir:
                node = node.childDir[i]
                if node.isDir == True:
                    return True
            else:
                return False
        return False

class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort(key=lambda e:len(e))
        trie = Trie()
        res = []
        for f in folder:
            if trie.isDelete(f) == False:
                res.append(f)
                trie.insert(f + '/')
        return res
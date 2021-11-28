class UnionFind:
    def __init__(self):
        self.father = {}
    
    def find(self,x):
        root = x
        while self.father[root] != None:
            root = self.father[root]
         
        return root
    
    def merge(self,x,y):
        root_x,root_y = self.find(x),self.find(y)
        
        if root_x != root_y:
            self.father[root_x] = root_y

    def is_connected(self,x,y):
        return self.find(x) == self.find(y)

    def add(self,x):
            self.father[x] = None


class Solution:
    def findRedundantConnection(self, edges):
        uf = UnionFind()
        for i in range(1, len(edges) + 1):
            uf.add(i)

        for node1, node2 in edges:
            if uf.is_connected(node1, node2) is False:
                uf.merge(node1, node2)
            else:
                return [node1, node2]

        return []
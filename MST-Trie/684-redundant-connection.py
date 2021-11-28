class UnionFind:
    def __init__(self, n):
        self.father = {}
        self.rank = [i for i in range(0, n+1)]
    
    def find(self,x):
        root = x
        while self.father[root] != None:
            root = self.father[root]
         
        return root
        
    def merge(self,x,y):
        root_x,root_y = self.find(x),self.find(y)

        if self.rank[root_x] < self.rank[root_y]:
            self.father[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.father[root_y] = root_x
        else:
            self.father[root_y] = root_x
            self.rank[root_x] += 1

    def is_connected(self,x,y):
        return self.find(x) == self.find(y)

    def add(self,x):
            self.father[x] = None
            self.rank[x] = 0

class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        uf = UnionFind(n)
        for i in range(1, len(edges) + 1):
            uf.add(i)

        for node1, node2 in edges:
            if uf.is_connected(node1, node2) is False:
                uf.merge(node1, node2)
            else:
                return [node1, node2]

        return []
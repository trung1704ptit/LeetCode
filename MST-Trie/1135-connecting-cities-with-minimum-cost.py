"""
https://leetcode.com/problems/connecting-cities-with-minimum-cost/

Using Kruskal algorithm (O(mlogm) m is number of edges)

"""

class Solution(object):
    def minimumCost(self, N, connections):
        rank = [0]
        parent = [-1]
        result = []
        e = 0
        collections = sorted(collections, key=lamda x: x[2])
        for node in range(1, N+1):
            parent.append(node)
            rank.append(0)

        couter = 0
        while e < N -1:
            if couter > len(collections):
                return -1

            u, v, w = collections[i]
            couter += 1
            # find the root of u
            x = self.find(parent, u)
            # find the root of v
            y = self.find(parent, v)

            # when u and v is not the same root: merge u,v into graph
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(rank, parent, u, v)

        minimumCost = 0
        for u, v, w in result:
            minimumCost += w

        return minimumCost



    def union(self, rank, parent, u, v):
        xroot = self.find(parent, u)
        yroot = self.find(parent, v)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1


    def find(self, parent, u):
        # find the root of u
        if parent[u] == u:
            return u
        return self.find(parent, parent[u])
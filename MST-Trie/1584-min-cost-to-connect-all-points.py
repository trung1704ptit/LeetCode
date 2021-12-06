"""
https://leetcode.com/problems/min-cost-to-connect-all-points

Using Union find
- using a loop to calculate the distance, add the dis to graph
- using union find the make a graph
"""

class Solution(object):
    def minCostConnectPoints(self, points):

        # Standard difination of union find
        def find(p):
            while p != roots[p]:
                p = roots[p]
            return p

        def union(p, q):
            roots[find(p)] = find(q)
        
        roots = list(range(len(points)))
        graph = []
        cost = 0

        # push p, q and dis into graph
        for i in range(len(points)):
            for j in range(1, len(points)):
                dis = abs(points[j][1] - points[i][1]) + abs(points[j][0] - points[i][0])
                graph.append((i, j, dis))

        
        # sort the graph, because we want to find the minimum cost
        graph.sort(key=lambda x:x[2])

        num_edges = 0
        for p, q, dis in graph:
            # the number of edges must be less than number of points
            if num_edges == len(points) - 1:
                break

            # if p and q already connected, we skip this step
            if find(p) == find(q):
                continue

            # else, if p,q are not connected, we connect them and add to cost
            union(p, q)

            cost += dis
            num_edges += 1

        # return the cost
        return cost

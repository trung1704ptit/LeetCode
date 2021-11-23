"""
- g: graph from given list and use prob value as weight
- q: priority queue
- insert(start, 1) into queue
- visited: a map to hold the visited node
- while q is not empty, do:
        (node, prob) = pop(q)
        if visited[node] > prob, then:
            go for next iteration
        otherwise:
            visited[node] = prob

        for each adjacent node adj and probability nextprob in g[node], do
            if visited[node] < prob * nextprob, then
                insert(adj, prob * nextprob) at the end of q
    return visited[end]
"""

from collections import defaultdict, deque

class Solution(object):
    def maxProbability(self, n, edges, successProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        g = defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i][0], edges[i][1]
            prob = successProb[i]
            g[src].append((dst, prob))
            g[dst].append((src, prob))

        q = deque()
        q.append((start, 1))
        visited = defaultdict(int)

        while q:
            node, prob = q.popleft()
            if visited[node] > prob:
                continue
            else:
                visited[node] =  prob

            for adj, nextProb in g[node]:
                if visited[adj] < prob * nextProb:
                    q.append((adj, prob * nextProb))
        return visited[end]  
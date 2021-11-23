"""
https://leetcode.com/problems/network-delay-time/
"""

import heapq
import collections

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        
        graph = collections.defaultdict(list)
        
        # make graph from input times
        for u, v, w in times:
            graph[u].append((v,w))
            
            
        # Q is min-heap of weight needed to reach the node
        Q = [[0, k]]
        
        
        # Dict to save time taken to reach each node {node:time taken}
        dist = collections.defaultdict(int)
        
        while Q:
            # pop the value with minimum weight
            time, node = heapq.heappop(Q)
            # when node is not visited:
            if node not in dist:
                dist[node] = time
                for v,w in graph[node]:
                    added_time = time + w
                    heapq.heappush(Q, [added_time, v])
                    
        # when all nodes are visited, find the maximum time needed to reach node
        if len(dist) == n:
            return max(list(dist.values()))
        # when not all nodes were visited, return -1
        return -1
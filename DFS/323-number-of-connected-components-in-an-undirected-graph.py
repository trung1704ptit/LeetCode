"""
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
"""


class Solution(object):
    def countComponents(self, n, edges):
        def dfs(node):
            if visited[node] == 1:
                return
            else:
                visited[node] = 1
                for node1, node2 in edges:
                    if node1 == node:
                        dfs(node2)
                    else:
                        dfs(node1)

        res = 0
        visited = [0 for i in range(n)]]
        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                res += 1

        return res
from collections import defaultdict
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        visited = set()
        adjList = defaultdict(list)
        count = 0
        
        def dfs(cur):
            visited.add(cur)
            for next in adjList[cur]:
                if next not in visited:
                    dfs(next)
        
        # build adjList
        i = 0
        for val in isConnected:
            for ii, val2 in enumerate(val):
                if val2 == 1:
                    adjList[i].append(ii)
            i += 1
            
        print(adjList)
            
        for index in range(len(isConnected[0])):
            if index not in visited:
                dfs(index)
                count +=1

        return count
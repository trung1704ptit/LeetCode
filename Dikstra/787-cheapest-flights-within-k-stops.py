from collections import defaultdict

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        pq = []
        for u, v, w in flights:
            graph[u].append((w, v))
            
        heapq.heappush(pq, (0, k+1, src))  # push (price, stops, city source)

        while pq:
            price, stops, city = heapq.heappop(pq)
            if city is dst: return price
            if stops > 0:
                for price_to_nei, nei in graph[city]:
                    heapq.heappush(pq, (price + price_to_nei, stops-1, nei))
        return -1
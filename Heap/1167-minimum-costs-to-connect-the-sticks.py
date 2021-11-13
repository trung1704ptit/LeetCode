"""
Solution:
- Using Min-Heap
push all element in list into heap
- we will pop heap ultil heap only has one element,
for each loop we will compute 2 element that pop from heap
a + b = c
c min when a min and b min
Pop 2 min element in heap to compute will give me a sum min
"""

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        res = 0
        while len(sticks) > 1:
            a = heapq.heappop(sticks)
            b = heapq.heappop(sticks)
            heapq.heappush(sticks, a + b)
            res += a + b
        return res
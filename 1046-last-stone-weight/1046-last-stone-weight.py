class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        x = 0
        y = 0
        heap = [- x for x in stones]
        heapq.heapify(heap)
        while heap:
            y = -heapq.heappop(heap)
            if heap:
                x = -heapq.heappop(heap)
            else:
                return y
            if y-x == 0:
                y = 0
                continue
            heapq.heappush(heap, -(y-x))
            y = y-x
        return y
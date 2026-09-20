class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for point in points:
            distance = ((point[0] - 0)**2 + (point[1] - 0)**2)
            heapq.heappush(heap, (distance, point[0], point[1]))
        
        result = []

        for _ in range(k):
            distance, x, y = heapq.heappop(heap)
            result.append([x,y])
        return result

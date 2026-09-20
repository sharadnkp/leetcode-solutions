class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for point in points:
            distance = ((point[0] - 0)**2 + (point[1] - 0)**2)
            heapq.heappush(heap, (-distance, point[0], point[1]))

            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []

        for distance, x, y in heap:
            result.append([x,y])
        return result

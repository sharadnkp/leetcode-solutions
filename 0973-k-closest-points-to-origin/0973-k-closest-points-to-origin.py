class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        result = []
        for point in points:
            distance = point[0]**2 + point[1]**2
            heapq.heappush(heap, (-distance, point))
            if len(heap)>k:
                heapq.heappop(heap)
            
        while heap:
            value, point = heapq.heappop(heap)
            result.append(point)
        return result 
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        job = sorted(zip(capital, profits))
        i = 0
        heap = []
        while k > 0:
            while i < len(job) and w >= job[i][0]:
                heapq.heappush(heap, -job[i][1])
                i += 1            
            
            if len(heap) == 0:
                return w

            curr_project = -heapq.heappop(heap) 
            w += curr_project
            k -= 1
        return w
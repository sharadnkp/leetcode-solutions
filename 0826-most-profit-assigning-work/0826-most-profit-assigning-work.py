class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        j = 0
        total = 0
        heap = []
        for i in worker:
            while j < len(jobs) and i >= jobs[j][0]:
                heapq.heappush(heap, -jobs[j][1])
                j+=1
            
            if not heap:
                total += 0
            else:
                x = heap[0]
                total += x
        
        return -total

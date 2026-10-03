class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort(key = lambda x:x[0])
        i, time = 0, tasks[0][0]
        heap, res = [],[]
        while heap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i+=1

            if not heap:
                time = tasks[i][0]
            else:
                procTime, index = heapq.heappop(heap)
                time += procTime
                res.append(index)        
        return res
class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        max_profit = 0
        worker.sort()
        j = 0
        total = 0
        for i in worker:
            while j < len(jobs) and i >= jobs[j][0]:
                max_profit = max(max_profit, jobs[j][1])
                j+=1
            total += max_profit
        return total
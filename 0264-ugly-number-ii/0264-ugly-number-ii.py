class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = {1}

        for _ in range(n):
            curr = heapq.heappop(heap)

            for factor in [2,3,5]:
                new_num = curr*factor

                if new_num not in seen:
                    seen.add(new_num)
                    heapq.heappush(heap, new_num)
        
        return curr
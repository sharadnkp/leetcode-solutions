class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        
        ans = 0

        for _ in range(k):
            res = -heapq.heappop(heap)
        
        return res
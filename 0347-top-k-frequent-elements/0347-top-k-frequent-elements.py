class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        
        heap = []
        for value,freq in freq.items():
            heapq.heappush(heap, (freq, value))
            if len(heap)>k:
                heapq.heappop(heap)
        
        result = []
        while heap:
            _, value = heapq.heappop(heap)
            result.append(value)

        return result
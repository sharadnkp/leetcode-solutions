class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dict1 = {}
        for num in nums:
            dict1[num] = dict1.get(num,0)+1
        
        heap = []
        for value,frequency in dict1.items():
            heapq.heappush(heap, (frequency, value))
            if len(heap)>k:
                heapq.heappop(heap)
            
        res = []
        while heap:
            freq, value = heapq.heappop(heap)
            res.append(value)
        
        return res



            
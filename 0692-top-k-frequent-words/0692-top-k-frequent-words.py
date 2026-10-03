import heapq
class Item:
    def __init__(self,freq,word):
        self.freq = freq
        self.word = word
    
    def __lt__(self,other):
        if self.freq!=other.freq:
            return self.freq<other.freq
        return self.word>other.word

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = {}
        for word in words:
            freq[word] = freq.get(word,0)+1
        
        heap = []
        result = []
        for word,freq in freq.items():
            heapq.heappush(heap,Item(freq,word))
            if len(heap)>k:
                heapq.heappop(heap)

        while heap:
            item = heapq.heappop(heap)
            result.append(item.word)
        
        return result[::-1]
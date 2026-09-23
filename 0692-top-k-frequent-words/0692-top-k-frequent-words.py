import heapq

class Item:
    def __init__(self, frequency, word):
        self.frequency = frequency
        self.word = word

    def __lt__(self, other):
        if self.frequency != other.frequency:
            return self.frequency < other.frequency

        return self.word > other.word


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:

        # 1. Count frequencies
        freq = {}

        for word in words:
            freq[word] = freq.get(word, 0) + 1

        # 2. Keep only k best words
        heap = []

        for word, frequency in freq.items():

            heapq.heappush(heap, Item(frequency, word))

            if len(heap) > k:
                heapq.heappop(heap)

        # 3. Extract the k words
        result = []

        while heap:
            item = heapq.heappop(heap)
            result.append(item.word)

        # Heap gives worst → best, so reverse
        result.reverse()

        return result
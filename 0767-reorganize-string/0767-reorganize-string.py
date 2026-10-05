class Solution:
    def reorganizeString(self, s: str) -> str:
        seat = 0
        res = []
        heap = []
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for word, frequency in freq.items():
            heapq.heappush(heap, (-frequency, word))

        while heap:
            freq1, word1 = heapq.heappop(heap)
            freq1 = -freq1

            if seat == 0 or res[seat - 1] != word1:
                res.append(word1)
                seat += 1
                freq1 -= 1

                if freq1 > 0:
                    heapq.heappush(heap, (-freq1, word1))

            else:
                if len(heap) == 0:
                    return ""

                freq2, word2 = heapq.heappop(heap)
                freq2 = -freq2

                res.append(word2)
                seat += 1
                freq2 -= 1

                if freq2 > 0:
                    heapq.heappush(heap, (-freq2, word2))

                heapq.heappush(heap, (-freq1, word1))

        return ''.join(res)
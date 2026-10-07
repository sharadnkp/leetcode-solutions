class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        start = 0
        end = 0
        last = {}
        result = []
        for i, ch in enumerate(s):
            last[ch] = i
        for i,ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                result.append(end-start+1)
                start = end+1
        return result

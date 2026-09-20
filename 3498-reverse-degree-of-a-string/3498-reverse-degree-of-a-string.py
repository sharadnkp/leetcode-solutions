class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i,ch in enumerate(s):
            total += (i+1) * (26 - (ord(ch)-97))
        return total
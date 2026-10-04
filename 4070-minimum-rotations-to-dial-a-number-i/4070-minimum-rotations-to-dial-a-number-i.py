class Solution:
    def minRotations(self, s: str) -> int:
        total = 0
        i = 0
        for digit in list(s):
            dist = min(abs(i-int(digit)), 10 - abs(i-int(digit)))
            i = int(digit)
            total += dist
        
        return total
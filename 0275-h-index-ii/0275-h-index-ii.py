class Solution:
    def isPossible(self, citations, guess):
        count = 0
        for i in citations:
            if i >= guess:
                count+=1
        return count >= guess

    def hIndex(self, citations: List[int]) -> int:
        ans = 0
        low = 0
        high = len(citations)
        while low <= high:
            guess = (low+high)//2
            if self.isPossible(citations, guess):
                ans = guess
                low = guess + 1
            else:
                high = guess - 1
        return ans
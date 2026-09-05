class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = 0
        while low<=high:
            guess = (low+high)//2
            count = 0
            for i in piles:
                count += (i + guess - 1)//guess
            if count<=h:
                ans = guess
                high = guess-1
            else:
                low = guess+1

        return ans
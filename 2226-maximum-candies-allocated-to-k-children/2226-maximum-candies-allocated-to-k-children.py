class Solution:
    def isPossible(self,candies,guess,k):
        count = 0
        for i in candies:
            count += i//guess
        return count >= k

    def maximumCandies(self, candies: List[int], k: int) -> int:
        low = 1
        high = sum(candies)//k
        ans = 0
        while low<=high:
            guess = (low+high)//2
            if self.isPossible(candies,guess,k):
                ans = guess
                low = guess+1
            else:
                high = guess-1
        return ans
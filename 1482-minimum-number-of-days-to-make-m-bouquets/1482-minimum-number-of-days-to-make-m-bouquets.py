class Solution:
    def isPossible(self, bloomDay, day, m, k):
        count = 0
        bouquets = 0

        for bloom in bloomDay:
            if bloom <= day:
                count += 1
                if count == k:
                    bouquets += 1
                    count = 0
            else:
                count = 0
            
        return bouquets >= m


    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m*k:
            return -1

        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1

        while low<=high:
            guess = (low+high)//2
            
            if self.isPossible(bloomDay, guess, m, k):
                ans = guess
                high = guess-1
            else:
                low = guess+1
        return ans

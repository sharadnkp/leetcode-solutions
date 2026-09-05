class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1
        while low<=high:
            guess = (low+high)//2
            adjacent = 0
            bouquets = 0
            for i in range(len(bloomDay)):
                if bloomDay[i]<=guess:
                    adjacent += 1
                    if adjacent == k:
                        bouquets += 1
                        adjacent = 0
                else:
                    adjacent = 0
            if bouquets>=m:
                ans = guess
                high = guess-1
            else:
                low = guess+1
        return ans

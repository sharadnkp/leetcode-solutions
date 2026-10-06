class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = 0
        while low <= high:
            mid = (low+high)//2
            i = 1
            total = 0
            for weight in weights:
                if total + weight > mid:
                    i += 1
                    total = 0
                total += weight
            
            if i > days:
                low = mid+1
            else:
                ans = mid
                high = mid-1
        return ans
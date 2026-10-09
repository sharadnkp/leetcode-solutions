class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cheap, best = inf, 0
        for price in prices:
            cheap = min(cheap, price)
            best = max(best, price - cheap)
        return best
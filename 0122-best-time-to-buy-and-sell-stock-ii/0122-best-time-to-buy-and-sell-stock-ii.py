class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        stack = []
        profit = 0
        for price in prices:
            if not stack or price <= stack[-1]:
                stack.append(price)
            else:
                profit += price - stack.pop()
                stack.append(price)
        return profit
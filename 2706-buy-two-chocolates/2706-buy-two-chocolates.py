class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        x = sorted(prices)
        y = sum(x[:2])
        if y>money:
            return money
        return money-y
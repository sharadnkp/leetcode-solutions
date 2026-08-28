class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.running = 1
        while self.stack and price >= self.stack[-1][0]:
            self.old_price, self.span = self.stack.pop()
            self.running += self.span
        self.stack.append((price,self.running))
        return self.running

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
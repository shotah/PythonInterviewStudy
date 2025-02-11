# class StockSpanner:
#     def __init__(self) -> None:
#         self.history: list[int] = []
#         return

#     def next(self, price: int) -> int:
#         # we need to check how many previous days are less than current price
#         # and then return the number of days it has been less than current
#         c = 1
#         for p in self.history:
#             if p > price:
#                 break
#             c += 1
#         self.history.insert(0, price)
#         return c


# leetcode expected code:
class StockSpanner:
    def __init__(self):
        self.stack = []  # Stack to store (price, span) pairs

    def next(self, price):
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            span += prev_span
        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
prices = [[100], [80], [60], [70], [60], [75], [85]]
prices = [[28], [14], [28], [35], [46], [53], [66], [80], [87], [88]]
for price in prices:
    param_1 = obj.next(price[0])
    print(param_1)

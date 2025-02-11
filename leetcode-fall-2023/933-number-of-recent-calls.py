class RecentCounter:
    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.pop(0)
        print(self.queue)
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()

print("Test 1")
# needs a list of pings to really test it.
for i in range(1, 10000, 1000):
    r = obj.ping(i)
r = obj.ping(10000)
print(r)

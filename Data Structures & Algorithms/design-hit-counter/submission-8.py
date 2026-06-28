class HitCounter:

    def __init__(self):
        self.hit_queue = collections.deque()
        self.limit = 300

    def hit(self, timestamp: int) -> None:
        self.hit_queue.appendleft(timestamp)

    def getHits(self, timestamp: int) -> int:
        print(timestamp)
        if not self.hit_queue:
            return 0
        print(f"{self.limit-timestamp}")
        while self.hit_queue and self.hit_queue[-1] <= timestamp-self.limit:
            print(self.hit_queue[-1])
            self.hit_queue.pop()
        
        return len(self.hit_queue)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)


# Dequeue
# hits go to the back , multiple hits in the same second. 
# during getHit(), check the oldest hit second, if its >300 seconds ago, pop until the first one is 300 seconds or less. , return the length
# incoming t, pop front until T(front) > 300-t
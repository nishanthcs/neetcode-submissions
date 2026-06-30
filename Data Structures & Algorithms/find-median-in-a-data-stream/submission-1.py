import heapq
class MedianFinder:

    def __init__(self):
        # max heap
        self.lower_heap = []
        # min heap
        self.upper_heap = []

    def addNum(self, num: int) -> None:
        # if incoming number is less than the maximum value in lower heap, insert it to lower.
        if not self.lower_heap or num <= -self.lower_heap[0]:
            heapq.heappush(self.lower_heap, -num)
        else:
            heapq.heappush(self.upper_heap, num)

        # rebalance sizes
        if len(self.lower_heap) > len(self.upper_heap) + 1:
            val = -heapq.heappop(self.lower_heap)
            heapq.heappush(self.upper_heap, val)
        elif len(self.upper_heap) > len(self.lower_heap) + 1:
            val = heapq.heappop(self.upper_heap)
            heapq.heappush(self.lower_heap, -val) 
        

    def findMedian(self) -> float:
        size_lower = len(self.lower_heap)
        size_upper = len(self.upper_heap)

        if size_lower < size_upper:
            return self.upper_heap[0]
        elif size_lower > size_upper:
            return -self.lower_heap[0]
        else:
            return (self.upper_heap[0]+(-self.lower_heap[0]))/2
        
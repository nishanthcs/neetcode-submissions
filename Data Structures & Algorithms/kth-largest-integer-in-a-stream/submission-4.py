class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)

        # only store the top k elements
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        # push the value to the heap
        heapq.heappush(self.heap, val)

        # Trim the heap to always hold top k
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)


        return self.heap[0]
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        # O(N)
        for num in nums:
            freq[num] += 1
        
        heap = []

        # O(K) where k is the max(N)
        for num,f in freq.items():
            # O(logK)
            heapq.heappush(heap, (f, num))

            if len(heap) > k:
                #O(logK)
                heapq.heappop(heap)
        
        # O(K)
        return [b[1] for b in heap]


# O(N), O(K*logK) where K <=N

# 
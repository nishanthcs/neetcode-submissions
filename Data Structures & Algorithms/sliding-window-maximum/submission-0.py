from collections import deque
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # you slide len(nums)-1-k times
        # and for each time, you send the slice and figure out the maxium. 
        # O(N-K)*O(K) runs 

        # Use a K sized Queue for the window
        # Heapify the queue every iteration O(K), get the max and store
        # update the queue and continue until i > N-k

        queue = deque()
        res = []

        for i,n in enumerate(nums):
            if len(queue) == k:
                # heapify
                listQ = [-num for num in queue]
                heapq.heapify(listQ)
                res.append(-heapq.heappop(listQ))
                # remove the left most to move the window
                queue.popleft()
            queue.append(n)

        # last window
        listQ = [-num for num in queue]
        heapq.heapify(listQ)
        res.append(-heapq.heappop(listQ))

        return res

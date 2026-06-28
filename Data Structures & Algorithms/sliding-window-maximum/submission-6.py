import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap=[]

        
        res: list[int] = []

        #O(N)
        for i,num in enumerate(nums):
            heapq.heappush(heap, (-num,i))
            
            # we push until the first window is ready
            if i >= k-1:
                # clear the heap of nums that are outside the boundary of the window
                left_boundary = i-k+1

                # O(logK)
                while heap and heap[0][1] < left_boundary:
                    popped_val, popped_idx = heapq.heappop(heap)
                    print(f"Popped {popped_val} (index {popped_idx} is out of bounds)")

                # we reaching the window, calculate the maximum O(1)
                max_win = -heap[0][0]
                res.append(max_win)

        
        return res

                
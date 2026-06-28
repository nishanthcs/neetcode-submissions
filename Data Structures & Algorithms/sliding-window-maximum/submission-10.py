class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonically decreasing queue to include just the max numbers
        queue = collections.deque()

        res = []

        for i,num in enumerate(nums):
            # Remove outside window items from the front. 
            if queue and queue[0] < i-k+1:
                queue.popleft()

            # Make queue decreasing upon adding the num 
            # if the existing values in the queues are less than the 
            # maximum , we remove them
            while queue and nums[queue[-1]] <= num:
                queue.pop()

            queue.append(i)

            # Check window and append res
            if i >= k-1:
                res.append(nums[queue[0]])

        return res
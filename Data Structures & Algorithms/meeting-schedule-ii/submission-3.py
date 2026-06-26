
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        # Start with 1 room
        # if there is a conflict, put that meeting in another room. 

        # Sort the intervals O(nlogn) 
        intervals.sort(key=lambda x: x.start)
        heap=[]

        heapq.heappush(heap, intervals[0].end)
        rooms = 1

        # if is sorted based on start time, the start of the ith meeting cannot be before the start of the i-1th meeting. 
        # O(N)
        for k in range(1, len(intervals)):
            # if there an overlap, instead of creating a room, check if a running meeting has ended. 
            if heap[0] <= intervals[k].start:
                # no overlap, reuse the room
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[k].end)
        
        return len(heap)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort in place
        intervals.sort(key=lambda x: (x[0],x[1]))

        # check if start(i+1) > end(i), no overlap
        i=1
        start=0
        end=1

        while i < len(intervals):
            # each loop you are comparing i with i-1th interval
            if intervals[i][start] > intervals[i-1][end]:
                # no overlap, lets look at the next one. 
                i += 1
            else:
                # overlap (or equal), assign the max of end
                final_end = max(intervals[i][end], intervals[i-1][end])
                intervals[i-1][end] = final_end
                # remove the ith interval since we merged it. 
                print("popping = ",intervals.pop(i))
        
        return intervals


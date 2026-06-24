class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort in place
        intervals.sort(key=lambda x: (x[0],x[1]))

        # write represents the last merged index. 
        # read is the value we compare it to.
        write=0
        read=1
        start=0
        end=1

        while read < len(intervals):
            if intervals[write][end] >= intervals[read][start]:
                # overlap, merge read into write. 
                intervals[write][end] = max(intervals[write][end], intervals[read][end])
                read += 1
            else:
                # no overlap, increment write. 
                write += 1
                # overwrite the stale interval with this read.
                intervals[write] = intervals[read]
                read += 1
        
        # Trim list coz slicing copies the sliced over to increasing space complexit
        del intervals[write+1:]

        return intervals


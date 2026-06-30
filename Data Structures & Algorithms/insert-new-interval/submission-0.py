class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Add before intervals
        result = []
        i = 0
        n = len(intervals)
        start = 0
        end = 1

        while i < n and intervals[i][end] < newInterval[start]:
            # the ith interval is before new interval
            result.append(intervals[i])
            i += 1
        

        # Merge overlapping end of ith interval is greater than start of the new interval
        # now we are checking if start of the ith interval <= end of new interval. if its greater, then this interval is after the new interval
        while i<n and intervals[i][start] <=  newInterval[end]:
            st = min(intervals[i][start],newInterval[start])
            ed = max(intervals[i][end], newInterval[end])
            # Overlapped interval
            newInterval = [st,ed]
            print(newInterval)
            i += 1
        
        # we found a spot where ith interval start > newInterval end , append the new interval
        result.append(newInterval)

        while i<n:
            result.append(intervals[i])
            i += 1


        return result 




        # Add after intervals


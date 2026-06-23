class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the array based on start time and then on end time ( if start timne is the same )
        # Go throught each interval and build the final list
        # push i0 to the list
        # compare i+1 with i in the list ; Compare end times. 
        # if E(i+1) == E(i) then finalE is max(Ei+1, Ei)
        # if E(i+1) < E(i) then finalE is E(i)
        # if E(i+1) > E(i) then finalE is E(i+1)
        # finaleE is max (E(i+1))

        start=0
        end=1
        # Sort the intervals based on start. which means, the incoming interval will already have starts sorted. 
        # O(nlogn) = Time complexity
        incoming_interval = sorted(intervals,key=lambda x: (x[start],x[end]))
        final_intervals = [incoming_interval[0]]
        final_idx = start

        # O(N)
        for i in range(1,len(incoming_interval)):
            if incoming_interval[i][start] > final_intervals[final_idx][end]:
                # no overlap. start is greater than end
                final_intervals.append(incoming_interval[i])
                final_idx +=1
            else:
                # There is overlap incoming_start < existing_final_end

                latest_interval = final_intervals.pop(final_idx)
                # Find out which of the end intervals is max and use it. 
                final_end = max(latest_interval[end], incoming_interval[i][end])
                latest_interval[end] = final_end

                final_intervals.append(latest_interval)
        
        return final_intervals
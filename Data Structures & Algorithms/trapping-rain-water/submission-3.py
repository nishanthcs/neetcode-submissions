class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        start,end = 0, len(height)-1
        lBoundary, rBoundary = height[start], height[end]
        t_water=0

        # Water trapped is governed by the smallest height between the boundaries.
        # L=0 ground; R=1, smallest is 0 
        # L=1 and R =3, smallest is 1 
        # capture boundaries at all times to figure out the water trapped in btween

        
        while start < end: # TODO Fix condition
            if lBoundary <= rBoundary:
                # find out the water level after left boundary
                start += 1
                ground_level_start = height[start]
                lBoundary = max(lBoundary, ground_level_start)
                t_water += lBoundary - ground_level_start
            else:
                # measure water trapped here
                end -= 1
                ground_level_end = height[end]
                rBoundary = max(rBoundary, ground_level_end)
                t_water += rBoundary - ground_level_end

        return t_water
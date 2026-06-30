class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_slice = 0
        max_sum = max(nums)

        for num in nums: 
            # what is the maximum sum until this index
            max_slice = max( max_slice + num, num )
            max_sum = max( max_slice, max_sum)

        
        return max_sum
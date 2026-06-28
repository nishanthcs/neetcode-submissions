class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # kadanes algorithm 
        # In Kadane's algorithm, variables serve very specific purposes:

    # curr_max (Local Maximum): What is the highest possible product of a subarray that ends right here, at this exact index?

    # curr_min (Local Minimum): What is the lowest possible product of a subarray that ends right here, at this exact index? (We track this because if we hit a negative number next, a massive negative curr_min suddenly becomes a massive positive curr_max).

    # global_max (Global Maximum): What is the highest product we have seen anywhere in the array so far?

        curr_max = 1
        
        curr_min = 1

        # O(N)
        global_max = max(nums)


        for i, num in enumerate(nums):
            # this is computing the product with max
            prod_max = curr_max * num
            # Computing the product with min 
            prod_min = curr_min * num

            curr_max = max(prod_max, prod_min, num)
            curr_min = min(prod_max, prod_min, num)

            global_max = max(curr_max, global_max)

            print(f"i={i}, num={num}, "f"prod_max={prod_max}, prod_min={prod_min}, "f"curr_max={curr_max}, curr_min={curr_min}, "f"global_max={global_max}")

        return global_max


        
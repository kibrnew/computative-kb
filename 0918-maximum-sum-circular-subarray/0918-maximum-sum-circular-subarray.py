class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        # Helper function to find maximum subarray sum
        def max_subarray_sum(nums):
            max_sum = float('-inf')
            current_sum = 0
            for num in nums:
                current_sum = max(num, current_sum + num)
                max_sum = max(max_sum, current_sum)
            return max_sum

        # Case 1: Maximum subarray sum without circular
        max_without_circular = max_subarray_sum(nums)

        # Case 2: Maximum subarray sum with circular
        # We can find this by calculating the maximum subarray sum of the inverted array
        # and subtracting it from the total sum of the original array.
        total_sum = sum(nums)
        inverted_nums = [-num for num in nums]
        max_with_circular = total_sum + max_subarray_sum(inverted_nums)

        # If all elements are negative, return the maximum subarray sum without circular
        if max_with_circular == 0:
            return max_without_circular

        # Return the maximum of the two cases
        return max(max_without_circular, max_with_circular)
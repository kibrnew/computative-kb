class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max = 0
        cur_min = 0
        _sum = 0
        max_sum = nums[0]
        min_sum = nums[0]
        for num in nums:
            cur_max = max(cur_max, 0) + num
            max_sum = max(max_sum, cur_max)
            cur_min = min(cur_min, 0) + num
            min_sum = min(min_sum, cur_min)
            _sum += num
        return max_sum if _sum == min_sum else max(max_sum, _sum - min_sum)
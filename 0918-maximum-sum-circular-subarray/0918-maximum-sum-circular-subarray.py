class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        def maxSum(nums):
            maxi= float('-inf')
            cur= 0
            for num in nums:
                cur= max(num, cur + num)
                maxi= max(maxi, cur)
            return maxi
        maxnc= maxSum(nums)
        total= sum(nums)
        nnums= [-num for num in nums]
        final= total + maxSum(nnums)
        if final== 0:
            return maxnc
        return max(maxnc,final)
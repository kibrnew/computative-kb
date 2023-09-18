class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        def maxSum(nums):
            maxSum = float('-inf')
            currSum = 0
            for num in nums:
                currSum = max(num, currSum + num)
                maxSum = max(maxSum, currSum)
            return maxSum

        maxWithoutCircular = maxSum(nums)

        totalSum = sum(nums)
        invertedNums = [-num for num in nums]
        maxWithCircular = totalSum + maxSum(invertedNums)

        if maxWithCircular == 0:
            return maxWithoutCircular

        return max(maxWithoutCircular, maxWithCircular)
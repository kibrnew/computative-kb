class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
            n = len(nums)
            nums.sort()
            count = [0] * (n + 1)
            for i, j in requests:
                count[i] += 1
                count[j + 1] -= 1
            for i in range(1, n + 1):
                count[i] += count[i - 1]
            ans = 0
            count.pop()
            count.sort()
            for i in range(len(nums)):
                ans += nums[i]*count[i]
            return ans % (10**9 + 7)
        

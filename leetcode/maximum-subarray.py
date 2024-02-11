class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi= float('-inf')
        cur= 0
        for num in nums:
            cur= max(num, cur + num)
            maxi= max(maxi, cur)
        return maxi

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*(n+1)
        for i in range(n):
            ans[i+1]=ans[i]+nums[i]
        return ans[1:]
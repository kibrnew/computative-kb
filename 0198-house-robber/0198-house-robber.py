class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        dp={}
        def recur(k):
            if k in dp :
                return dp[k]
            if k==1:
                return max(nums[0],nums[1])
            if k==0:
                return nums[0]
            dp[k]=max(nums[k]+recur(k-2),recur(k-1))
            return dp[k]
        return recur(n-1)
        
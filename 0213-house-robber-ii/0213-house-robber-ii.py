class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        dp={}
        def recur(k,end):
            # if k==1:
            #     return max(nums[0],nums[1])
            if k==end:
                return nums[end]
            if k<end:
                return 0
            # if k==0:
            #     return nums[0]
            if k in dp :
                return dp[k]
            dp[k]=max(nums[k]+recur(k-2,end),recur(k-1,end))
            return dp[k]
        left=recur(n-1,1)
        dp={}
        right=recur(n-2,0)
        return max(left,right)
        
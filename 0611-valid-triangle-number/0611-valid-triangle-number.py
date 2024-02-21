class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        ans=0
        n=len(nums)
        for i in range(n-2):
            for j in range(i+1,n):
                val=nums[i]+nums[j]
                ind=bisect_right(nums,val-1)
                ans+=max(0,ind-j-1)
        return  ans
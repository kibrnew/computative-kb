class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        ans=0
        n=len(nums)
        for i in range(n-2):
            if nums[i]==0:
                continue 
            for j in range(i+1,n):
                val=nums[i]+nums[j]-1
                ind=bisect_right(nums,val)
                ans+=ind-j-1
        return  ans
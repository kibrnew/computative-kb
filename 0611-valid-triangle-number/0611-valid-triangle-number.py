class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        ans=0
        n=len(nums)
        for i in range(n-2):
            if nums[i]==0:
                continue 
            for j in range(i+1,n):
                val=nums[i]+nums[j]
                ind=bisect_left(nums,val)-1
                ans+=ind-j
        return  ans
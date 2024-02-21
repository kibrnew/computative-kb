class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        ans=nums[0]
        n=len(nums)
        s=nums[0]
        for i in range(1,n):
            s+=nums[i]
            ans=max(ans,(s+i)//(i+1))
        return ans
            
            
        
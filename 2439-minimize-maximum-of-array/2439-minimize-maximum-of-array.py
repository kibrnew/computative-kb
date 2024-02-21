class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        ans=0
        n=len(nums)
        s=0
        for i in range(n):
            s+=nums[i]
            ans=max(ans,(s+i)//(i+1))
        return ans
            
            
        
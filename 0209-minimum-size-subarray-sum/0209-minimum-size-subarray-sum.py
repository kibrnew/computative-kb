class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        ans=float("inf")
        l=0
        n=len(nums)
        s=0
        for r in range(n):
            s+=nums[r]
            while target<=s:
                ans=min(ans,r-l+1)
                s-=nums[l]
                l+=1
                
        if ans==float("inf"):
            return 0
        return ans
            
       
                
            
                
            
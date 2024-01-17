class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        n=len(nums)
        l=0
        ans=0
        for r in range(n):
            k-=(1-nums[r])
            while k<0:
                k+=(1-nums[l])
                l+=1
            ans=max(ans,r-l+1)
            
        return ans 
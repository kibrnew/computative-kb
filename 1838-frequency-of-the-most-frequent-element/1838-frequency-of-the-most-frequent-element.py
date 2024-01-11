class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        n=len(nums)
        left=0
        ans=1
        
        for right in range(1,n):
            k-=(nums[right]-nums[right-1])*(right-left)
            
            while k<0:
                k+=(nums[right]-nums[left])
                left+=1
            
            ans=max(ans,right-left+1)
        return ans
                
                
            
            
        
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        l=0
        n=len(nums)
        count=0
        ans=0
        if 1 not in nums:
            return 0
        for r in range(n):
            count+=(1-nums[r])
            while count>1:
                count+=(nums[l]-1)
                l+=1
            ans=max(ans,r-l)
        return ans
       
                    
            
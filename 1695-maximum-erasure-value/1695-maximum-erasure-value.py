class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        count=Counter()
        n=len(nums)
        l=0
        s=0
        ans=0
        for r in range(n):
            count[nums[r]]+=1
            s+=nums[r]
            while count[nums[r]]>1:
                count[nums[l]]-=1
                s-=nums[l]
                l+=1
            ans=max(ans,s)
        return ans
                
        
       
                
            
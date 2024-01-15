class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        ans=0
        l=0
        n=len(nums)
        count=0
        prev=0
        for r in range(n):
            count+=nums[r]%2
            if count==k:
                prev=0
            while count==k:
                prev+=1
                count-=nums[l]%2
                l+=1
            ans+=prev
        return ans
                
        
   
        
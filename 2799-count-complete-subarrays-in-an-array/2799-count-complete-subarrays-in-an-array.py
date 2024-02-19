class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        k=len(set(nums))
        n=len(nums)
        l=0
        count=Counter()
        ans=0
        for r in range(n):
            count[nums[r]]+=1
            while len(count)==k:
                ans+=n-r
                count[nums[l]]-=1
                if count[nums[l]]==0:
                    count.pop(nums[l])
                l+=1
            
        return ans
            
        
            
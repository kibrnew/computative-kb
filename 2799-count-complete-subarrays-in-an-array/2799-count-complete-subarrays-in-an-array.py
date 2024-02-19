class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        k=len(set(nums))-1
        n=len(nums)
        l=0
        count=Counter()
        ans=0
        for r in range(n):
            count[nums[r]]+=1
            while len(count)>k:
                count[nums[l]]-=1
                if count[nums[l]]==0:
                    count.pop(nums[l])
                l+=1
            ans+=r-l+1
        return n*(n+1)//2-ans
            
        
            
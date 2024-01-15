class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        count = Counter()
        l=r=0
        ans=0
        for val in nums:
            count[val]+=1
            if len(count)>k:
                count.pop(nums[r])
                r+=1
                l=r
            
            if len(count)==k:
                while count[nums[r]]>1:
                    count[nums[r]]-=1
                    r+=1
                ans+=r-l+1
        return ans
            
        
        
                
       
        
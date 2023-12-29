class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        count=Counter(nums)
        key=sorted(count.keys())
       
        ans=0
        
        for i,val in enumerate(key):
            ans+=i*count[val]
        return ans 
            
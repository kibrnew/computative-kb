class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        n=len(nums)
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]+nums[i]
            
        count=Counter()
        ans=0
        for val in prefix:
            ans+=count[val%k]
            count[val%k]+=1
        return ans
            
            
        


        
        
       
        
                
     
            
        
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
         
        count=Counter()
        count[0]=1
        ans=0
        val=0
        for vv in nums:
            val+=vv
            ans+=count[val%k]
            count[val%k]+=1
        return ans
            
            
        


        
        
       
        
                
     
            
        
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
         
        count={}
        count[0]=1
        ans=0
        val=0
        for vv in nums:
            val+=vv
            ans+=count.get(val%k,0)
            if val%k not in count:
                count[val%k]=0
            count[val%k]+=1
        return ans
            
            
        


        
        
       
        
                
     
            
        
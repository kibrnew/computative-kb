class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
         
        count={}
        count[0]=1
        ans=0
        val=0
        for vv in nums:
            val+=vv
            ind=val%k
            ans+=count.get(ind,0)
            if ind not in count:
                count[ind]=0
            count[ind]+=1
        return ans
            
            
        


        
        
       
        
                
     
            
        
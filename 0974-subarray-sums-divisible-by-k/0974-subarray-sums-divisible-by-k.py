class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        prefix=list(accumulate(nums))
        for i in range(n):
            prefix[i]=prefix[i]%k
        count = defaultdict(int)
        ans=0
        for num in prefix: 
            if num==0:
                ans+=1
            ans+=count[num]
            count[num]+=1
        return ans


        
        
       
        
                
     
            
        
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        prefix=list(accumulate(nums))
        for i in range(n):
            prefix[i]=prefix[i]%k
        count = defaultdict(int)
        ans=0
        for num in prefix: 
            r=num%k
            if r==0:
                ans+=1
            if count[r]:
                ans+=count[r]
            count[num]+=1
        return ans
#         ans=0
#         for i in  
        
#         cnt = 0

        
        
       
        
                
     
            
        
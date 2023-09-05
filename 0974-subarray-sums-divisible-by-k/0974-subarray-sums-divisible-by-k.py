class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=(prefix[i]+nums[i])%k
        count = defaultdict(int)
        ans=0
        for num in prefix[1:]: 
            if num==0:
                ans+=1
            ans+=count[num]
            count[num]+=1
        return ans


        
        
       
        
                
     
            
        
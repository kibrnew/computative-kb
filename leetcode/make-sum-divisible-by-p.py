class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        s=sum(nums)
        target=s%p
        if target==0:
            return 0
        ind=Counter()
        ind[target]=-1
        s=0
        ans=float("inf")
        for i,val in enumerate(nums):
            s+=val
            s%=p
            if s in ind:
                ans=min(ans,i-ind[s])
                
            # print(ind,s,i)
                
            ind[(s+target)%p]=i
            
        if ans==len(nums):
            return -1
        return ans
            
                
            
        
        
        
        
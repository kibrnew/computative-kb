class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        n=len(nums)
        prefix=[0]*(n+1)
        
        for l,r in requests:
            prefix[r+1]-=1
            prefix[l]+=1
        prefix.pop()
            
        for i in range(1,n):
            prefix[i]+=prefix[i-1]
        
        nums.sort()
        prefix.sort()
        ans=0
        for i in range(n):
            ans+=prefix[i]*nums[i]
            ans%=(10**9+7)
            
        return ans
            
        
        
        
        
        
        
        

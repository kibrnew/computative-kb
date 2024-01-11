class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        s=sum(nums[:k])
        ans=s
        n=len(nums)
        
        for i in range(n-k):
            s-=nums[i]
            s+=nums[i+k]
            ans=max(ans,s)
            
        return ans/k
        
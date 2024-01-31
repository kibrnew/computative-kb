class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]+nums[i]
            
        ans=[]
        for i in range(n):
            left=nums[i]*i-prefix[i]
            right=prefix[-1]-prefix[i+1]-nums[i]*(n-i-1)
            ans.append(left+right)
        return ans
            
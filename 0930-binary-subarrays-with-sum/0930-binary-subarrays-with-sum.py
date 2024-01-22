class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        n=len(nums)
        prefix=[0]*(n+1)
        
        for i in range(n):
            prefix[i+1]+=prefix[i]+nums[i]
            
        count=defaultdict(int)
        ans=0
        for val in prefix:
            ans+=count[val]
            count[val+goal]+=1
        return ans 
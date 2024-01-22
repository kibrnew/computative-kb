class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        n=len(nums)
        count=Counter()
        s=0
        ans=0
        count[goal]+=1
        for i in range(n):
            s+=nums[i]
            ans+=count[s]
            count[s+goal]+=1
            
        return ans
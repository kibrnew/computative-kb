class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        n=len(nums)
        count=Counter()
        s=0
        ans=0
        count[0]+=1
        for i in range(n):
            s+=nums[i]
            ans+=count[s-goal]
            count[s]+=1
            
        return ans
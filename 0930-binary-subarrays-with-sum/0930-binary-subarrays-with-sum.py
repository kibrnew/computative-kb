class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        n=len(nums)
        nums.append(0)
        s=0
        count=defaultdict(int)
        ans=0
        for i in range(-1,n):
            s+=nums[i]
            ans+=count[s]
            count[s+goal]+=1
        return ans
            
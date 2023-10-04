class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans=Counter(nums)
        for i in range(1,len(nums)+1):
            if ans[i]>=1:
                ans[i]-=1
            else:
                t=i
        for i in ans:
            if ans[i]>=1:
                now=i
        return [now,t]
        
            
        
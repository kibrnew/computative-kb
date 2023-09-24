class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        prefix=[0]*(n+1)
        ans=[]
        for i in range(n):
            prefix[i+1]=prefix[i]+nums[i]
        for q in queries:
            ind=bisect_left(nums,q)
            add=q*ind-(n-ind)*q
            to=prefix[-1]-2*prefix[ind]
            ans.append(add+to)

        return ans
        
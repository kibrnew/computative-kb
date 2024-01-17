class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
#         prefix=[0]*(n+1)
        
#         for i in range(n):
#             prefix[i+1]=prefix[i]+nums[i]

        count=Counter()
        count[k]=1
        ans=0
        val=0
        for vv in nums:
            val+=vv
            rest=k+val
            ans+=count[val]
            count[rest]+=1
        # print(count)
        return ans
        
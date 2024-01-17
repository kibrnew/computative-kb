class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
#         prefix=[0]*(n+1)
        
#         for i in range(n):
#             prefix[i+1]=prefix[i]+nums[i]

        count={}
        count[k]=1
        ans=0
        val=0
        for vv in nums:
            val+=vv
            rest=k+val
            ans+=count.get(val,0)
            if rest not in count:
                count[rest]=0
 
            count[rest]+=1
        # print(count)
        return ans
        
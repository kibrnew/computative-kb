class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        prefix=[0]+list(accumulate(nums))
        ans=[]
        for x in queries:
            i=bisect_left(nums,x)
            ans.append(x*(2*i-n)+prefix[n]-2*prefix[i])

        return ans 
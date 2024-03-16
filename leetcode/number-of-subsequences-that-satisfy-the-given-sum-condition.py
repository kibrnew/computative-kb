class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=0

        for i,val in enumerate(nums):
            if target-val<val:
                break
            n=max(bisect_right(nums,target-val)-i,0)
            if n>0:
                n-=1
                ans+=pow(2,n,1000000007)



        return ans%1000000007

        # for
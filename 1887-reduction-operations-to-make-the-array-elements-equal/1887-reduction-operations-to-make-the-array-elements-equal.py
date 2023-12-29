class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        nums.sort()
        n=len(nums)
        val=0
        ans=0
        
        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                val+=1
            ans+=val
        return ans
            
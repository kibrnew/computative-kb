class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        ans=float("inf")
        n=len(nums)
        for i in range(n-k+1):
            ans=min(ans,nums[i+k-1]-nums[i])
        return ans
            
        
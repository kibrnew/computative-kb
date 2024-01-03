class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        n=len(nums)
        left=0
        right=n-1
        ans=0
        nums.sort()
        
        while left<right:
            if nums[left]+nums[right]>=target:
                right-=1
            else:
                left+=1
            ans+=left
        return ans
                
        
class Solution:
    def canJump(self, nums: List[int]) -> bool:       
        maxi=0
        n=len(nums)
        for i in range(n):
            if maxi<i:
                return False
            maxi=max(maxi,nums[i]+i)
        
        
        return True 
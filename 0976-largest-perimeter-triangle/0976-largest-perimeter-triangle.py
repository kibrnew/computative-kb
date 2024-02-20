class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans=0
        n=len(nums)
        for i in range(n-2):
            temp=nums[i+1]+nums[i+2]
            if nums[i]<temp and ans==0:
                return nums[i]+temp
        return ans
            
        
        
        
        
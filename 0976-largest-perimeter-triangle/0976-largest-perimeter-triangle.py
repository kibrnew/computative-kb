class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        nums.append(float("inf"))
        i=0
        while nums[i]>=nums[i+1]+nums[i+2]:
            i+=1
        ans=sum(nums[i:i+3])
        if ans==float("inf"):
            return 0
        return ans
        
        
        
        
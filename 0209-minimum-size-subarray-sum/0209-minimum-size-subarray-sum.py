class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pr2 = 1
        pr1= 1
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        nums = [0]+nums
        ans = len(nums)+1

        while pr2<len(nums):
            while nums[pr2]-nums[pr1-1] >= target:
                ans = min(ans, pr2-pr1+1)
                pr1+=1
            pr2+=1

        if ans == len(nums)+1:
            return 0
        return ans
       
                
            
                
            
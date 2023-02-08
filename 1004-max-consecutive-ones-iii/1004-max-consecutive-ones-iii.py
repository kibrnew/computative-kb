class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        pr1 = 0
        for i in range(len(nums)):
            if nums[i]==0:
                k -=1
            if k < 0:
                if nums[pr1]==0:
                    k = k+ 1
                pr1 += 1
        ans=i - pr1 +1 
        return ans
            
        
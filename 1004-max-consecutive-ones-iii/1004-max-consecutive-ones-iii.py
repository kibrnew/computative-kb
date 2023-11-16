class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        pr1 = 0
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                k -=1
            if k < 0:
                if nums[pr1]==0:
                    k = k+ 1
                pr1 += 1
        ans=n-pr1
        return ans
            
        
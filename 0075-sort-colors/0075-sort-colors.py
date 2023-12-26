class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ans=[0]*3
        for val in nums:
            ans[val]+=1
            
        new=[ ]
        for i in range(3):
            new.extend([i]*ans[i])
            
        nums[::]=new[::]
        
        return nums
            
                


        
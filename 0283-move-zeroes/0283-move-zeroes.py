class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=0
        n=len(nums)
        
        while left<n and right<n:
            while left<n and nums[left]!=0:
                left+=1
            while right<n and (nums[right]==0 or right<=left): 
                right+=1
            if left<n and right<n:
                nums[left],nums[right]=nums[right],nums[left]
            
                    
                    
           
                    
            
        
            
            
            
        
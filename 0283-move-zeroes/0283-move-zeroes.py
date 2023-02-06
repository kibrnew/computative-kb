class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1=0
        p2=0
        s=len(nums)
        while p1<s:
            k=0
            if nums[p1]==0:
                p1= p1+1
            
            if p1 < s:
                if nums[p1]==0:
                    k=-1
                if p1>p2 and nums[p1]!=0:
                    if p1 < s:
                        temp=nums[p1]
                        nums[p1]=nums[p2]
                        nums[p2]=temp
            p1=p1+1
            p2=p2+1+k
                    
                    
           
                    
            
        
            
            
            
        
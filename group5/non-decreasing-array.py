class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        count=0
        n=len(nums)
        ind=n
        for i in range(n-1,0,-1):
            if nums[i]<nums[i-1]:
                count+=1
                ind=i-1
                
        if count>=2:
            return False
        
        if count==1:
            
            arr1=list(nums)
            arr2=list(nums)
            arr1.pop(ind)
            arr2.pop(ind+1)
            
            f1=True
            f2=True
            
            for i in range(n-2):
                if arr1[i]>arr1[i+1]:
                    f1=False
        
                if arr2[i]>arr2[i+1]:
                    f2=False
                    
            return f1 or f2
        
        return True
            
       
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        n=len(nums)
        
        for i in range(n):
            
            if type(nums[i]) is str:
                continue
                
            ind=i+nums[i]
           
            
            sig=nums[i]//abs(nums[i])
            nums[i]=str(i+1)
    
            # print(nums)
            while i!=ind%n and type(nums[ind%n]) ==int and  nums[ind%n]//abs(nums[ind%n])==sig:
                # print("here",i)
                prev=ind%n
                ind+=nums[prev]
                nums[prev]=str(i+1)
                if ind%n==prev:
                    break
                
                if nums[ind%n]==str(i+1):
                    return True
                
        return False
                
                
            
        
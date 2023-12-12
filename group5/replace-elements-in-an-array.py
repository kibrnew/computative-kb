class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        ind={}
        
        for i,val in enumerate(nums):
            ind[val]=i
            
        for replaced,val in operations:
            
            i=ind[replaced]
            
            nums[i]=val
            
            ind[val]=i
            
        return nums
        
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        ind={}
        
        for i,val in enumerate(nums):
            ind[val]=i
            
        for i,val in operations:
            nums[ind[i]]=val
            ind[val]=ind[i]
            
        return nums
        
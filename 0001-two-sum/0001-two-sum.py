class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        rev={}
        
        for i,val in enumerate(nums):
            diff=target-val
            if diff in rev:
                return [i,rev[diff]]
            rev[val]=i
            
       
        
        
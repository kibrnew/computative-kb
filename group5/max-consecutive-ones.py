class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        
        new=[str(val) for val in nums]
        s="".join(new)
        count=len(max(s.split("0"),key=len))
       
        return count
        
        
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count=1
        ans=nums[0]
        
        for val in nums[1:]:
            
            if val!=ans:
                count-=1
            else:
                count+=1
                
            if count==0:
                count=1
                ans=val
                
        return ans
        
                
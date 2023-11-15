class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        s=sum(nums)
        n=len(nums)
        temp=0
        for i in range(n):
            if s-nums[i]==temp:
                return i
            temp+=nums[i]
            s-=nums[i]
        return -1
                
            
            
        
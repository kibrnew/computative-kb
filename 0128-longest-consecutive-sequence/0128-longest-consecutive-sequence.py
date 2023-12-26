class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums.sort()
        
        count=1
        ans=1
        if len(nums)==0:
            return 0
        temp=nums[0]
        
        for val in nums[1:]:
            if val==temp+1:
                count+=1
            elif val==temp:
                continue
            else:
                count=1
            
            ans=max(ans,count)
            temp=val
            
        return ans
                
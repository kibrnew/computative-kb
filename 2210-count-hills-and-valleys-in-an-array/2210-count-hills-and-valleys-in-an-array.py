class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        i=1
        ans=0
        if nums[i-1]==nums[i]:
            while nums[i]==nums[i-1] and i<len(nums)-1:
                i+=1
        if nums[i-1]<nums[i]:
            uflag=True
        else :
            uflag=False
        print(i)
        while i < len(nums)-1:
            if uflag :
                if nums[i]>nums[i+1]:
                    ans+=1
                    uflag=False
            else :
                if nums[i]<nums[i+1]:
                    ans+=1
                    uflag=True
            i+=1
        return ans 
                    
                    
            
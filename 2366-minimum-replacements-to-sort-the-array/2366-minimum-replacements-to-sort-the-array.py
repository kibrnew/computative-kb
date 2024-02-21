class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        nums=nums[::-1]
        
        maxi=nums[0]
        ans=0
        for val in nums:
            cur=(val+maxi-1)//maxi
            ans+=cur-1
            maxi=val//cur
        return ans
        
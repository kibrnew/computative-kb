class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        s=sum(nums)
        cur=0
        for i,val in enumerate(nums):
            s-=val
            if cur==s:
                return i
            cur+=val
        return -1
        
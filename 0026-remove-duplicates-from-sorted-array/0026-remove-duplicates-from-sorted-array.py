class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans=set(nums)
        ans2=list(ans)
        ans2.sort()
        nums[:]=ans2
        return len(ans2)
                
                
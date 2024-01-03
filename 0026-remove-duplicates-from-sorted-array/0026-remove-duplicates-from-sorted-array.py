class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans=[nums[0]]
        prev=nums[0]
        for val in nums[1:]:
            if prev!=val:
                ans.append(val)
            prev=val
        nums[:]=ans[:]
        return len(ans)
                
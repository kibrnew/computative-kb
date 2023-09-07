class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        s = []
        ans= 0
        for i, a in enumerate(nums):
            if not s or nums[s[-1]] > a:
                s.append(i)
        print(s)
        for j in reversed(range(len(nums))):
            while s and nums[s[-1]] <= nums[j]:
                ans= max(ans, j - s.pop())
        return ans
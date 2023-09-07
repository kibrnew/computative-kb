class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []

        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        width = 0
        for i in reversed(range(n)):
            print(i)
            if not stack:
                break
            while stack and stack[-1] > i:
                stack.pop()
            while stack and nums[stack[-1]] <= nums[i]:
                width = max(width, i - stack.pop())

        return width
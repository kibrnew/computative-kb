class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [0] * n
        stack = []
        for i in reversed(range(n)):
            while stack and nums[i] > nums[stack[-1]]:
                ans[i] = max(ans[i] + 1, ans [stack.pop()])
                # print(ans)
                # print(stack)
            stack.append(i)
            # print(stack)
        return max(ans)
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans, stack = 0, []
        for num in arr:
            cnt = 1
            while stack and stack[-1][0] >= num:
                n, c = stack.pop()
                ans += n*c*cnt
                cnt += c
            stack.append((num, cnt))
        cnt = 1
        while stack:
            n, c = stack.pop()
            ans += n * c * cnt
            cnt += c
        return ans % (10**9 + 7)
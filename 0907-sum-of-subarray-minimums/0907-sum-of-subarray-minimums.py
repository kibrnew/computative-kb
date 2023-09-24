class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans=0
        stack=[]
        for num in arr:
            count = 1
            while stack and stack[-1][0]>=num:
                n, c = stack.pop()
                ans+=n*c*count
                count += c
            stack.append((num,count))
        count = 1
        while stack:
            n,c=stack.pop()
            ans+=n*c*count
            count+=c
        return ans%(10**9 + 7)
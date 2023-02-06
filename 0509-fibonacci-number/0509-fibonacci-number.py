class Solution:
    def fib(self, n: int) -> int:
        dp=[0,1]
        for i in range(1,n):
            dp.append(dp[-1]+dp[-2])
        return dp[n]
        
        
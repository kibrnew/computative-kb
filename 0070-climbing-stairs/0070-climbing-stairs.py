class Solution:
    def climbStairs(self, n: int) -> int:
        
        # @cache
        # def fib(k):
        #     if k<=1:
        #         return 1
        #     else :
        #         return fib(k-1)+fib(k-2)
        fib=[1,1]
        for i in range(1,n):
            fib.append(fib[i]+fib[i-1])
        return fib[n]
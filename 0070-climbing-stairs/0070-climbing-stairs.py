class Solution:
    def climbStairs(self, n: int) -> int:
        
        # @cache
        # def fib(k):
        #     if k<=1:
        #         return 1
        #     else :
        #         return fib(k-1)+fib(k-2)
        fib=[1,2]
        for i in range(2,n):
            fib.append(fib[i-1]+fib[i-2])
        return fib[n-1]
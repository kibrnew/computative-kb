class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def fib(k):
            if k<=1:
                return 1
            else :
                return fib(k-1)+fib(k-2)
        return fib(n) 
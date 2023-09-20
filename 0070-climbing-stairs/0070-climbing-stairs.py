class Solution:
    def climbStairs(self, n: int) -> int:
        
        # @cache
        # def fib(k):
        #     if k<=1:
        #         return 1
        #     else :
        #         return fib(k-1)+fib(k-2)
        pr1=1
        pr2=1
        for i in range(n):
            pr1,pr2=pr1+pr2,pr1
        return pr2
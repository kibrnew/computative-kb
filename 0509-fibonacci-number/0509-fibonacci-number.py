class Solution:
    def fib(self, n: int) -> int:
        @cache
        def fibon(k):
            if k<=1:
                return k 
            return fibon(k-1)+fibon(k-2)
        return fibon(n)
        
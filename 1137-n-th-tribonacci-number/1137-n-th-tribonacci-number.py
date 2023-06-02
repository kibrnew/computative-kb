class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def tri(k):
            if k<=1:
                return k
            if k==2:
                return 1
            return tri(k-1)+tri(k-2)+tri(k-3)
        return tri(n)
        
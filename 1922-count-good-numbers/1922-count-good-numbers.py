class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(k,n,m):
            if n==0:
                return 1
            if n==1:
                return k%m
            if n%2==1:
                return (power(k,n//2,m)**2*(k%m))%m
            else:
                return power(k,n//2,m)**2%m
        ans= power(20, n//2, 10**9 + 7)
        if n%2==1: 
            ans*=5
        return ans%(10**9+7)
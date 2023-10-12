class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        def power(a,b,m):
            result=1
            
            while b>0:
                if b&1:
                    result=((result%m)*(a%m))%m
                a=(a*a)%m
                b>>=1
            return result
        
        evens=5
        odds=4 
        
        return (power(evens,(n+1)//2,10**9 + 7)*power(odds,n//2,10**9 + 7))%(10**9 + 7)
        
        
            
            
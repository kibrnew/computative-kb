class Solution:
    def myPow(self, x: float, n: int) -> float:


        def power(n):
            if n==0:
                return 1
            if n==1:
                return x

            res=power(n//2)
            res*=res

            if n%2:
                res*=x
            return res


        if n<0:
           return  1/power(-n)
        return power(n)

        
                    
            
            
            
            
        
        
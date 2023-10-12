class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def power(a,b):
            result=1
            
            while b>0:
                if b&1:
                    result*=a
                a*=a
                b>>=1
            return result
        if n<0:
            return 1/power(x,-n)
        return(power(x,n))
        
                    
            
            
            
            
        
        
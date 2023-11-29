class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        p=int(log(n)/log(3))
        div=3**p
        # print(div)
        for i in range(p,-1,-1):
            # print(div,n)
            if div*2<=n:
                return False
            if div<=n:  
                n-=div
            
            div//=3
            
            
            
        return True

            
        
        
        
        
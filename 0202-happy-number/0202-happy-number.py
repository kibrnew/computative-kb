class Solution:
    def isHappy(self, n: int) -> bool:
        
        def ssum(m):
            
            return sum([int(val)**2 for val in str(m)])
        
        for _ in range(7):
            n=ssum(n)
        return n==1
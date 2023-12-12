class Solution:
    def isHappy(self, n: int) -> bool:
        visited=set()
        
        def ssum(m):
            
            return sum([int(val)**2 for val in str(m)])
        
        while n!=1:
            
            n=ssum(n)
            if n in visited:
                return False
            visited.add(n)
            
        return True
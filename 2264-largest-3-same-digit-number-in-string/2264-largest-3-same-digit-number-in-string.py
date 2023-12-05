class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n=10
        
        for i in range(n-1,-1,-1):
            if str(i)*3 in num:
                return str(i)*3
            
        return ""
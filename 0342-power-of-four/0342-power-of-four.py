class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        x=n
        while x>3:
            if x==4:
                return True
            x=x/4
        return False
        
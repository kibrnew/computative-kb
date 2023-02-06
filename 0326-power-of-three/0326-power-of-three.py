class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True
        x=n
        while x>2:
            if x==3:
                return True
            x=x/3
        return False
        
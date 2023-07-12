class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right=x
        if x==1:
            return 1
        while (right-left)>1:
            mid=left+(right-left)//2
            temp=mid**2
            if temp==x:
                return mid
            elif temp>x:
                right=mid
            else :
                left=mid
        return left 
            
            
        
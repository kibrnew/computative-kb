class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x=num
        left=0
        right=x
        if x==1:
            return True
        while (right-left)>1:
            mid=left+(right-left)//2
            temp=mid**2
            if temp==x:
                return True
            elif temp>x:
                right=mid
            else :
                left=mid
        return left**2==num
        
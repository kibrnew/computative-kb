# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left=0
        x=n
        right=x
        while (right-left)>1:
            mid=left+(right-left)//2
            temp=guess(mid)
            if temp==0:
                return mid
            elif temp==-1:
                right=mid
            else :
                left=mid
        if (right-left)==1:
            if guess(right)==0:
                return right 
            else :
                return left 
        return left
            
        
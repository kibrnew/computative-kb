# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left=0
        x=n
        right=x
        while (right-left)>1:
            mid=left+(right-left)//2
            temp=isBadVersion(mid)
            if temp:
                right=mid
            else :
                left=mid
        return right
            
        
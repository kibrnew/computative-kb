class Solution:
    def arrangeCoins(self, n: int) -> int:
        k=int(sqrt(2*n))
        s=(k+1)*k//2
        if s>n:
            return k-1
        return k
        
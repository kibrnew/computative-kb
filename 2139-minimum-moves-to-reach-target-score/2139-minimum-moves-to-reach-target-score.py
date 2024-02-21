class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        k=maxDoubles
        ans=0
        while target>1 and k>0:
            ans+=target%2
            target//=2
            ans+=1
            k-=1
        return target-1+ans
        
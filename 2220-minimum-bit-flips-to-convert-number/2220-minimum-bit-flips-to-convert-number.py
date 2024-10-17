class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans=start^goal
        res=0
        while ans:
            res+=ans&1
            ans>>=1
        return res 

        
        
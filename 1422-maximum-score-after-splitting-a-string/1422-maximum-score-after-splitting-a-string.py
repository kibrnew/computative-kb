class Solution:
    def maxScore(self, s: str) -> int:
        n=len(s)
        right=s.count("1")
        left=0
        ans=0
        for i in range(n-1):
            if s[i]=="0":
                left+=1
            else:
                right-=1
            ans=max(ans,left+right)
        return ans
            
        
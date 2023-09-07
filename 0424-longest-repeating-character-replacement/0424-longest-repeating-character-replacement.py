class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c=defaultdict(int)
        l=0
        n=len(s)
        m=0
        ans=0
        for r in range(n):
            c[s[r]]+=1
            m=max(m,c[s[r]])
            if (r-l+1)-m>k:
                c[s[l]]-=1
                l+=1  
            ans=max(ans,r-l+1)
        return ans 
                


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l=0
        n=len(s)
        ans=0
        count=Counter()
        
        for r in range(n):
            count[s[r]]+=1
            while r-l+1-max(count.values())>k:
                count[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans
            


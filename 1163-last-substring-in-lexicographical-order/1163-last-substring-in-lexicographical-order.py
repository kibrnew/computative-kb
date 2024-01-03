class Solution:
    def lastSubstring(self, s: str) -> str:
        
        k=0
        for val in s:
            k=max(k,ord(val))
            
        ans=""
        for i in range(len(s)):
            if ord(s[i])==k:
                ans=max(ans,s[i:])
        
    
        return ans
        
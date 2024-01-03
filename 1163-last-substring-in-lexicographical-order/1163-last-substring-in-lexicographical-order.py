class Solution:
    def lastSubstring(self, s: str) -> str:
        
        maxi=max(s)
        sol = ""
        first = s.index(maxi)
        for i in range(first, len(s)):
            if s[i]==maxi:
                sol = max(sol, s[i:])
    
        
        return sol    
                
            
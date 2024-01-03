class Solution:
    def lastSubstring(self, s: str) -> str:
        
        maxi=max(s)
        ans = []
        for i in range(len(s)):
            if s[i]==maxi:
                ans.append(i)
        sol = ""
        for n in ans:
            sol = max(sol, s[n:])
        
        return sol
        
            
                
            
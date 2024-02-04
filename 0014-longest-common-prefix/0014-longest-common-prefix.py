class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        n=len(strs)
        m=len(strs[0])
        
        for val in strs:
            m=min(m,len(val))
            
        ans=""
        for i in range(m):
            target=strs[0][i]
            for j in range(n):
                if strs[j][i]!=target:
                    return ans
            ans+=target
            
        return ans
                
                
        
        
            
            
        
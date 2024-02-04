class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ans=strs[0]
        
        for val in strs:
            temp=""
            for i in range(min(len(val),len(ans))):
                if val[i]==ans[i]:
                    temp+=val[i]
                else:
                    break
            ans=temp
        return ans
        
        
            
            
        
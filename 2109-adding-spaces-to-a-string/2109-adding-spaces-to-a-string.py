class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        ans=[" "]*(len(s)+len(spaces))
        
        spaces=set(spaces)
        offset=0
        
        for i in range(len(s)):
            
            if i in spaces:
                offset+=1
            ans[i+offset]=s[i]
            
        return "".join(ans)
        
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()
        m=len(s)
        ans=0
        i=0
        
        for val in g:
            cur=0
            while i<m and cur<val:
                cur=s[i]
                i+=1
                
            if cur>=val:
                ans+=1

                
        return ans
            
        
       
        
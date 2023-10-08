class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans=0
        pr1=0
        pr2=0
        ans=0
        while pr1<len(g) and pr2<len(s):
            if s[pr2]>=g[pr1]:
                ans+=1
                pr2+=1
            else :
                while pr2<len(s) and s[pr2]<g[pr1]:
                    pr2+=1
                if pr2<len(s) and s[pr2]>=g[pr1]:
                    ans+=1
                    pr2+=1
                    
            pr1+=1
        return ans 
            
        
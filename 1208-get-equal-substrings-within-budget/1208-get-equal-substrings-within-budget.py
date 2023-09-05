class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l=[]
        for i in range(len(s)):
            l.append(abs(ord(s[i])-ord(t[i])))
        n=len(l)
        pr1=pr2=temp=ans=0
        print(l)
        while pr2<n and pr1<n:
            temp+=l[pr2]
            while temp>maxCost:
                temp-=l[pr1]
                pr1+=1
            ans=max(ans,pr2-pr1+1)
            pr2+=1        
        return ans 
                
            
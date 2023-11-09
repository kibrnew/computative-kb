class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        n=len(s)
        v={"a","e","i","o","u"}
        
        ind=[]
        for i in range(n):
            if s[i].lower() in v:
                ind.append(i)
        
        for i in range(len(ind)//2) :
            s[ind[i]],s[ind[-1-i]]=s[ind[-1-i]],s[ind[i]]
        return "".join(s)
        
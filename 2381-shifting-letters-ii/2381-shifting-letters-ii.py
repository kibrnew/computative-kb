class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        n=len(s)
        ans=[0]*(n+1)
        
        for a,b,d in shifts:
            if d==0:
                ans[a]-=1
                ans[b+1]+=1
            else:
                ans[a]+=1
                ans[b+1]-=1
                
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=ans[i]+prefix[i]
        # print(prefix)
        res=[]  
        off=ord("a")
        for i in range(n):
            res.append(chr(off+(ord(s[i])-off+prefix[i+1])%26))
        return "".join(res)
                
        
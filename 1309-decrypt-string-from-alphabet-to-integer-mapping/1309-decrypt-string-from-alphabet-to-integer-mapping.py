class Solution:
    def freqAlphabets(self, s: str) -> str:
        s=s[::-1]
        o=96
        ans=[]
        n=len(s)
        i=0
        while i<n:
            val=s[i]
            if val=="#":
                ans.append(chr(o+int(s[i+2:i:-1])))
                i+=2
            else:
                ans.append(chr(o+int(val)))
            i+=1
        return "".join(ans[::-1])
        
                
            
           
            
        
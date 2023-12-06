class Solution:
    def printVertically(self, s: str) -> List[str]:
        ans=[]
        words=s.split()
        n=len(words)
        maxi=len(max(words,key=len))
        
        for i in range(maxi):
            temp=[]
            for val in words:
                if i<len(val):
                    temp.append(val[i])
                else:
                    temp.append(" ")
            for val in temp[::-1]:
                if val==" ":
                    temp.pop()
                else:
                    break
            ans.append("".join(temp))
        return ans
            
        
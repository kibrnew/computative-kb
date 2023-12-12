class Solution:
    def reverseWords(self, s: str) -> str:
        temp=s.split(" ")
        ans=[]
       
        for val in temp[::-1]:
            if val :
                ans.append(val)
                
        return " ".join(ans)
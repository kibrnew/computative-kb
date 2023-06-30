class Solution:
    def removeStars(self, s: str) -> str:
        k=[]
        for i in s:
            if i=="*":
                k.pop()
            else:
                k.append(i)
        return "".join(k)
            
        
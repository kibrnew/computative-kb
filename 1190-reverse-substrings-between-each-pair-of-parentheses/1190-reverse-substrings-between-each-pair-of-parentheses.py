class Solution:
    def reverseParentheses(self, s: str) -> str:
        wstack=list(s)
        p=s.count("(")
        for q in range(p):
            ind=wstack.index(")")
            for i in range(ind,-1,-1):
                if wstack[i]=="(":
                    break 
            wstack.pop(ind)
            wstack.pop(i)
            w=wstack[i:ind-1]
            w.reverse()
            wstack[i:ind-1]=w
        ans="".join(wstack)
        return ans 
        
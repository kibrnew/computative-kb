class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if (len(s)%2)!=0:
            return False 
        if s[0]=="]" or s[0]==")" or s[0]=="}":
            return False      
        for i in range(len(s)):
            if s[i]=="[" or s[i]=="(" or s[i]=="{":
                stack.append(s[i])
            else:
                if stack:
                    cb= s[i]
                    op= stack.pop()
                    jo=op+cb
                    if (jo!="[]") and (jo!="{}") and (jo!="()"):
                        return False
                else:
                    return False
        if len(stack) >0 :
            return False
            
        return True
            
            
            
            
        
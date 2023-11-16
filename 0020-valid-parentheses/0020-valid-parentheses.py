class Solution:
    def isValid(self, s: str) -> bool:
        
        closes={"{":"}","[":"]","(":")"}
        stack=[]
        for val in s:
            if val in closes:
                stack.append(val)
            else:
                if not stack or closes[stack.pop()]!=val:
                    return False
        if stack:
            return False
        return True 
            
       
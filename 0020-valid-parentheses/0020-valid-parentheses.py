class Solution:
    def isValid(self, s: str) -> bool:
        
        # stack=list(s)
        opens={"{":"}","[":"]","(":")"}
        stack=[]
        
        for val in s:
            if val not in opens:
                if stack and opens[stack.pop()]==val:
                    continue 
                return False
            else:
                stack.append(val)
        if stack:
            return False
        return True
            
       
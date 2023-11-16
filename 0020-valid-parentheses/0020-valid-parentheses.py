class Solution:
    def isValid(self, s: str) -> bool:
        
        opens={"}":"{","]":"[",")":"("}
        stack=[]
        for val in s:
            if val not in opens:
                stack.append(val)
            else:
                if not stack or opens[val]!=stack.pop():
                    return False
        if stack:
            return False
        return True 
            
       
class Solution:
    def removeStars(self, s: str) -> str:
        
        stack=[]
        
        for val in s:
            if stack and val == "*":
                stack.pop()
            else:
                stack.append(val)
                
        return "".join(stack)
       
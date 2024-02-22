class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[]
        left="{[("
        right="}])"
        
        for val in s:
            
            if val in left:
                stack.append(val)
                
            else:
                ind=right.index(val)
                if stack and stack[-1]==left[ind]:
                    stack.pop()
                else:
                    return False
        return not(stack)
            
            
     
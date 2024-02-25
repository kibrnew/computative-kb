class Solution:
    def simplifyPath(self, path: str) -> str:
        
        new=path.split("/")
        stack=[]
        
        for val in new:
            if not val or val==".":
                continue 
                
            if val=="..":
                if stack:
                    stack.pop()  
                else:
                    continue
            else:
                stack.append("/"+val)
                
        if not stack:
            return "/"
                
        return "".join(stack)
        
            
            
        
        
class Solution:
    def isValid(self, s: str) -> bool:
        
        # stack=list(s)
        opens={"{":"}","[":"]","(":")"}
        closed={"}","]",")"}
        stack=[]
        
        for val in s:
            if val in closed:
                if stack and opens[stack.pop()]==val:
                    continue 
                return False
            else:
                stack.append(val)
        if stack:
            return False
        return True
            
        
        
        
        
        # n=len(s)
        # if len(s)&1:
        #     return False
        # while stack:
        #     right=stack.pop()
        #     if  right in closed:
        #         left=stack.pop()
        #         if left not in opens or opens[left]!=right:
        #             return False
        #     else:
        #         return False
     
        # return True
            
            
            
            
            
        
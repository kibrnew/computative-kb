class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        i=1
        n=len(typed)
        
        if name[0]!=typed[0]:
            return False
        
        for val in name[1:]:
            
            if i<n and val==typed[i]:
                i+=1
            else:
                while i<n and typed[i]==typed[i-1]:
                    i+=1
                    
                if i<n and typed[i]==val:
                    i+=1
                else:
                    return False
                
        while i<n and typed[i]==typed[i-1]:
                i+=1
        if i<n:
            return False
        return True 
                    
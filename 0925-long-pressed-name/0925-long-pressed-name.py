class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i=0
        j=0
        n=len(name)
        m=len(typed)
        
        while i<n or j<m:
            
            if i<n and j<m and name[i]==typed[j]:
                i+=1
                j+=1
            else:
                if 0<j<m and typed[j]==typed[j-1]:
                    j+=1
                else:
                    return False
        return True
                    
            
        
        
                
            
        
        
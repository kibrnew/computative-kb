class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        n=len(name)
        m=len(typed)
        i=0
        j=0
        
        cm=0
        ct=0
        
        while i<n or j<m:
            previ=i
            prevj=j
            
            if i<n and j<m and name[i]==typed[j]:
                
                i+=1
                j+=1
                
                while i<n and name[i]==name[i-1]:
                    i+=1
                    
                while j<m and typed[j]==typed[j-1]:
                    j+=1
                    
                if i-previ>j-prevj:
                    return False
                
            else:
                return False
            
        return True 
                
            
        
        
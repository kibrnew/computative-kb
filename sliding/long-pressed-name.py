class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        i=0
        n=len(name)
        prev=0
        
        for val in typed:
            if i<n and name[i]==val:
                i+=1
                
            elif val==prev:
                continue
                
            else:
                return False
            prev=val
            
        return i==n
        
                    
            
        
        
                
            
        
        
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        
        ans=abs(target[0])+abs(target[1])
        
        for x,y in ghosts:
            
            if abs(target[0]-x)+abs(target[1]-y) <=ans:
                return False
            
        return True
        
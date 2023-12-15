class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
        visited=set()
        
        for a,b in zip(fronts,backs):
            
            if a==b:
                visited.add(a)
                
                
        ans=float("inf") 
        
        for a,b in zip(fronts,backs):
    
            if a not in visited:
                ans=min(ans,a)
            if b not in visited:
                ans=min(ans,b)
        if ans==float("inf"):
            return 0
        else :
            return ans 
            
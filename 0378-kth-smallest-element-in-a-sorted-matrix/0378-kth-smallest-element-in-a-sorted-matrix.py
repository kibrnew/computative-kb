class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        new=[]
        for col in matrix:
            new.extend(col)
        new.sort()
        return new[k-1]
            
            
            
        
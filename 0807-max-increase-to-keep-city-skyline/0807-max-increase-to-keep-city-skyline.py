class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        
        n=len(grid)
        m=len(grid[0])
        row=defaultdict(int)
        col=defaultdict(int)
        
        for i in range(n):
            for j in range(m):
                row[i]=max(row[i],grid[i][j])
                col[j]=max(col[j],grid[i][j])
                
        ans=0
                
        for i in range(n):
            for j in range(m):
                val=min(row[i],col[j])
                ans+=val-grid[i][j]
        return ans 
                
                
        
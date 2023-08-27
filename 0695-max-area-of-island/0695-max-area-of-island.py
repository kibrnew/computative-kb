class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def check(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])
        def dfs(r,c):
            grid[r][c]=2
            direction=[(0,1),(1,0),(0,-1),(-1,0)]
            ans=1
            for dr,dc in direction:
                row=dr+r
                col=dc+c
                if check(row,col) and grid[row][col]==1:
                    ans+=dfs(row,col)
            return ans
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    ans=max(ans,dfs(i,j))
        return ans 
        
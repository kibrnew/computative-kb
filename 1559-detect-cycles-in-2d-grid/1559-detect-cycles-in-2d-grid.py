class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        def check(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])
        def dfs(r,c,pr,pc,val):
            grid[r][c]=val.upper()
            for dr,dc in directions:
                row=dr+r
                col=dc+c
                if check(row,col):
                    if (row,col)==(pr,pc):
                        continue
                    if grid[row][col]==val.upper():
                        return True
                    if grid[row][col]==val and dfs(row,col,r,c,val):
                        return True
            return False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]>"Z" and  dfs(i,j,-1,-1,grid[i][j]):
                    return True
        return False

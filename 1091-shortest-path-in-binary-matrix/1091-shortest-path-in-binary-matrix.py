class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions=[(1,1),(1,0),(0,1),(-1,0),(0,-1),(1,-1),(-1,1),(-1,-1)]
        n = len(grid)
        if grid[0][0]!=0 or grid[n-1][n-1] != 0:
            return -1
        if len(grid)==1:
            return 1
        def check(row,col):
            return 0<=row<n and  0<=col<n
        visited = [[False] * n for _ in range(n)]
        queue=deque()
        queue.append((0,0,1))
        while queue:
            r,c,pos=queue.popleft()
            grid[r][c]=2
            for dr,dc in directions:
                row=dr+r
                col=dc+c
                if check(row,col)and not visited[row][col] and grid[row][col]==0 :
                    if (row,col)==(n-1,n-1):
                        return pos+1
                    queue.append((row,col,pos+1))
                    visited[row][col] = True
    
        return -1
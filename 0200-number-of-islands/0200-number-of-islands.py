class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=set()
        directions4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count=0
        def valid(row,col):
            n=len(grid)
            m=len(grid[0])
            return 0<=row<n and 0<=col<m
        def bfs(i,j):
            visited.add((i,j))
            queue=deque()
            queue.append((i,j))
            while queue:
                row,col=queue.pop()
                for dr,dc in directions4:
                    newr,newc=row+dr,col+dc
                    if valid(newr,newc) and (newr,newc) not in visited and grid[newr][newc]=="1":
                        queue.append((newr,newc))
                        visited.add((newr,newc))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and (i,j) not in visited:
                    bfs(i,j)
                    count+=1
        return count

                        
                        
        
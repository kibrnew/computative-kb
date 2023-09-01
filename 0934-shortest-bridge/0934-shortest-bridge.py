class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        for i,arr in enumerate(grid ):
            if 1 in arr:
                start=(i,arr.index(1))
        def check(row, col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        visited=set()
        def dfs(r,c):
            visited.add((r,c))
            for dr,dc in directions:
                row=dr+r
                col=dc+c
                if check(row,col) and grid[row][col]==1:
                    if (row,col) not in visited:
                        dfs(row,col)
        row,col=start
        dfs(row,col)
        ans=float("inf")
        for ones in visited:
            queue=deque([(ones,0)])
            vis=set()
            while queue:
                t,dist=queue.popleft()
                r,c=t
                flag=0
                for dr,dc in directions:
                    row=r+dr 
                    col=c+dc
                    if check(row,col) and (row,col) not in vis:
                        if grid[row][col]==0:
                            vis.add((row,col))
                            queue.append(((row,col),dist+1))
                        elif (row,col) not in visited:
                            flag=1
                            break
                else :
                    continue 
                break 
            if dist==0 or flag==0:
                continue
            ans=min(ans,dist)
#             print(dist)
            
#         print(ans)         
#         print(visited)
        return ans
                
            
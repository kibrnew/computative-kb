class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        

        directions=[(0,1),(1,0),(-1,0),(0,-1)]

        def check(r,c):
            return 0<=r<len(board) and 0<=c<len(board[0])

       
        def dfs(row,col,temp):
            if not temp:
                return True

            if board[row][col]!=temp[0]:
                return False
            temp=temp[1:]
            if not temp:
                return True
            vis.add((row,col))
            for dr,dc in directions:
                r=dr+row
                c=dc+col
                if check(r,c) and (r,c) not in vis and  dfs(r,c,temp):
                    return True 

            vis.remove((row,col))

            return False

        n=len(board)
        m=len(board[0])
        for i in range(n):
            for j in range(m):
                vis=set()
                if dfs(i,j,word):
                    return True 
        return False

        

        
        
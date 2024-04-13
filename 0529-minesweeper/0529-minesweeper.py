class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def check(row,col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        def count(row, col):
            count = 0
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if check(r,c) and board[r][c] == 'M':
                    count += 1
            return count
        def dfs(row, col):
            if board[row][col] == 'E':
                adjacent = count(row, col)
                if adjacent == 0:
                    board[row][col] = 'B'
                    for dr, dc in directions:
                        r = row + dr
                        c = col + dc
                        if check(r,c):
                            dfs(r, c)
                else:
                    board[row][col] = str(adjacent)

      

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        row,col = click

        if board[row][col] == 'M':
            board[row][col] = 'X'
        else:
            dfs(row,col)

        return board
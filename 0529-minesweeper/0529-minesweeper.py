class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def dfs(row, col):
            if board[row][col] == 'M':
                board[row][col] = 'X'
            elif board[row][col] == 'E':
                mines_adjacent = count_adjacent_mines(row, col)
                if mines_adjacent == 0:
                    board[row][col] = 'B'
                    for dr, dc in directions:
                        r, c = row + dr, col + dc
                        if 0 <= r < len(board) and 0 <= c < len(board[0]):
                            dfs(r, c)
                else:
                    board[row][col] = str(mines_adjacent)

        def count_adjacent_mines(row, col):
            count = 0
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 'M':
                    count += 1
            return count

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        click_row, click_col = click

        if board[click_row][click_col] == 'M':
            # If the click hits a mine, game over.
            board[click_row][click_col] = 'X'
        else:
            # If the click is on an empty square, reveal it and its neighbors.
            dfs(click_row, click_col)

        return board

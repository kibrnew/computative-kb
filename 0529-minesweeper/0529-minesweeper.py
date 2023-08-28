class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # Define directions for adjacent squares
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        def count_adjacent_mines(row, col):
            count = 0
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 'M':
                    count += 1
            return count

        def reveal_blank(row, col):
            if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == 'E':
                mines_adjacent = count_adjacent_mines(row, col)
                if mines_adjacent == 0:
                    board[row][col] = 'B'
                    for dr, dc in directions:
                        reveal_blank(row + dr, col + dc)
                else:
                    board[row][col] = str(mines_adjacent)

        click_row, click_col = click

        if board[click_row][click_col] == 'M':
            # If the click hits a mine, game over.
            board[click_row][click_col] = 'X'
        else:
            # If the click is on an empty square, reveal it and its neighbors.
            reveal_blank(click_row, click_col)

        return board

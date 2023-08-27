class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0]) if grid else 0
        visited = [[False] * n for _ in range(m)]
        memo = [[None] * n for _ in range(m)]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c, parent_r, parent_c, char):
            if memo[r][c] is not None:
                return memo[r][c]

            visited[r][c] = True

            for dr, dc in directions:
                row, col = r + dr, c + dc

                if 0 <= row < m and 0 <= col < n and grid[row][col] == char:
                    if (row, col) == (parent_r, parent_c):
                        continue

                    if visited[row][col] or dfs(row, col, r, c, char):
                        memo[r][c] = True
                        return True

            visited[r][c] = False
            memo[r][c] = False
            return False

        for r in range(m):
            for c in range(n):
                if not visited[r][c]:
                    if dfs(r, c, -1, -1, grid[r][c]):
                        return True

        return False

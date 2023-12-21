class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        ans=0
        for r in range(n-2):
            for c in range(m-2):
                ans=max(ans,sum(grid[r][c:c+3])+grid[r+1][c+1]+sum(grid[r+2][c:c+3]))
        return ans
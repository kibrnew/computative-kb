class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans=0
        for i in grid:
            idx = bisect_right(i[::-1],-1)
            ans+=idx
        return ans
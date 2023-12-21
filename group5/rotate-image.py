class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ans=list(map(list,zip(*matrix)))
        for i in range(len(ans)):
            matrix[i][::]=ans[i][::-1]
        
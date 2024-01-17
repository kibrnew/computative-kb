class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n=len(matrix)
        m=len(matrix[0])
        self.s=[[0]*(m+1) for _ in range(n+1)]
        
        for i in range(n):
            for j in range(m):
                self.s[i+1][j+1]=self.s[i+1][j]+self.s[i][j+1]-self.s[i][j]+matrix[i][j]
                
        
        # print(self.s) 
                

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        cur=self.s[row2+1][col2+1]-self.s[row1][col2+1]-self.s[row2+1][col1]+self.s[row1][col1]
        return cur
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
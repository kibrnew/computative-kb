class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        n=len(mat)
        m=len(mat[0])
        ans=[[] for _ in range( (n+m))]
        
        for i in range(n):
            for j in range(m):
                ans[i+j].append(mat[i][j])
             
        res=[]
        for i,val in enumerate(ans):
            if i%2==0:
                res.extend(val[::-1])
            else:
                res.extend(val)
        return res
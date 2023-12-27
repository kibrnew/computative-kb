class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        grid=[ [0]*n for _ in range(m)]
        
        for i,j in guards:
            grid[i][j]=1
            
        for i,j in walls:
            grid[i][j]=2
            
        
        def helper(matrix):
            
            r=len(matrix)
            c=len(matrix[0])
            ans=0
            
            for i in range(r):
                
                flag=False
                count=c
                prev=0
                
                for j in range(c):
                    
                    if matrix[i][j]==2:
                        prev=0
                        flag=False
                        
                    elif matrix[i][j]==1:
                        count-=prev
                        for k in range(prev):
                            matrix[i][j-k-1]=-1
                        prev=0 
                        flag=True
                        
                    elif matrix[i][j]==0:
                        if flag:
                           
                            matrix[i][j]=-1
                           
                        else:
                            count+=1
                            prev+=1
                            
                    count-=1
                ans+=count
                
            return matrix,ans                    
                    
            
        grid,ans1=helper(grid)   
        rev=list(map(list,zip(*grid)))
        grid,ans2=helper(rev)
        
        return ans2
        
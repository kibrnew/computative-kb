class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        i_start=0
        i_end=len(matrix)-1
        j_start=0
        j_end=len(matrix[0])-1
        
        i_direction=True 
        j_direction=True
        ans=[]
        for _ in range(min(len(matrix),len(matrix[0]))):
            if j_direction:
                j=j_start
                while j<=j_end:
                    ans.append(matrix[i_start][j])
                    j+=1
                i_start+=1
                j_direction=False

            else:
                j=j_end
                while j>=j_start:
                    ans.append(matrix[i_end][j])
                    j-=1
                i_end-=1
                j_direction=True 


            if i_direction:
                i=i_start
                while i<=i_end:
                    ans.append(matrix[i][j_end])
                    i+=1
                j_end-=1
                i_direction=False
            else:
                i=i_end
                while i>=i_start:
                    ans.append(matrix[i][j_start])
                    i-=1
                j_start+=1
                i_direction=True
        return ans
                
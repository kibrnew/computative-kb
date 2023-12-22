class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row=defaultdict(set)
        col=defaultdict(set)
        box=defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                val=board[i][j]
                
                if val!=".":
                    k=(i//3)*10+j//3
                    if val in row[i] or val in col[j] or val in box[k]:
                        return False
                    row[i].add(val)
                    col[j].add(val)
                    box[k].add(val)
        # print(box)
                    
        return True
                
                
                
                
                
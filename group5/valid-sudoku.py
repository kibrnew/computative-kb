class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n=len(board)
        m=len(board[0])
        
        for i in range(n):
            count=defaultdict(int)
            rcount=defaultdict(int)
            for j in range(m):
                
                if board[i][j]!= ".":
                    count[board[i][j]]+=1
                    
                if board[j][i]!=".":
                    rcount[board[j][i]]+=1
            c=list(count.values())+list(rcount.values())  
            if c:
                maxi=max(c)
        
                if maxi>1:
                    return False
        
        for i in range(0,n,3):
            
            for j in range(0,n,3):
                temp=[]
                temp.extend(board[i][j:j+3])
                temp.extend(board[i+1][j:j+3])
                temp.extend(board[i+2][j:j+3])
                count=Counter(temp)
                count.pop(".")
                if count:
                    maxi=max(count.values())
                    if maxi >1:
                        return False
        return True 
                
                
                
                
                
                
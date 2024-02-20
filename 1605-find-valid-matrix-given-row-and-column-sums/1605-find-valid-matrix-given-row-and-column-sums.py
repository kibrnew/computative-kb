class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        
        ans=[]
        for val in rowSum:
            temp=[]
            for i,cur in enumerate(colSum):
                if cur>=val:
                    temp.append(val)
                    colSum[i]-=val
                    val=0
                else:
                    temp.append(cur)
                    val-=cur
                    colSum[i]=0
            ans.append(temp)

        return ans 
                    
                    
        
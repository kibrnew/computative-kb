class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        def pascal(l):
            if l<=1:
                return [1]*(l+1)
            new=pascal(l-1)
            ans=[1]
            for i in range(1,len(new)):
                ans.append(new[i]+new[i-1])
            ans.append(1)
            return ans

        return pascal(rowIndex)
                
        
                
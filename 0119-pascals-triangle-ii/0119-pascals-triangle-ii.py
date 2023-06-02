class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def pascal(l):
            if rowIndex<=1:
                return [1]*(rowIndex+1)
            if len(l)==rowIndex+1:
                return l
            for i in range(len(l)-1):
                l[i]=l[i]+l[i+1]
            l.insert(0,1)
            return pascal(l)
        return pascal([1,2,1])
                
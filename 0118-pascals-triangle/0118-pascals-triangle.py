class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        temp=[]
        def pascal(l):
            temp.append(l)
            if numRows==len(l):
                return 
            ans=[1]
            for i in range(1,len(l)):
                ans.append(l[i]+l[i-1])
            ans.append(1)
            return pascal(ans)
        pascal([1])
        return temp
                
            
        
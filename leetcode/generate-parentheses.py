class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        temp=[]
        def dfs(opend,closed):
            if opend==closed==0:
                ans.append("".join(temp))
    
            
            if opend>0:
                temp.append("(")
                dfs(opend-1,closed)
                temp.pop()

            if opend<closed:
                temp.append(")")
                dfs(opend,closed-1)
                temp.pop()
        dfs(n,n)
        return ans 


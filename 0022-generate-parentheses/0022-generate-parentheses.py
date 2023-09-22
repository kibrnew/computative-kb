class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        @cache
        def dfs(cur, opened, closed):
            if len(cur) == 2 * n:
                ans.append(cur)
                return
            if opened< n:
                dfs(cur + '(', opened + 1, closed)
            if closed < opened:
                dfs(cur + ')', opened, closed + 1)
                
        dfs("", 0, 0)
        return ans

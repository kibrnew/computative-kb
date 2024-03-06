class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        letter=["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

        temp=[]
        ans=[]
        def dfs(i):
            if i==len(digits):
                ans.append("".join(temp))
                return 

            for val in letter[int(digits[i])-2]:
                temp.append(val)
                dfs(i+1)
                temp.pop()

        if len(digits)==0:
            return []

        dfs(0)
        return ans
        
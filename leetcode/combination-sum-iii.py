class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        ans=[]
        temp=[]
        
        def backtrack(i):
            if len(temp)>k:
                return 
            if len(temp)==k and sum(temp)==n:
                ans.append(list(temp))
                return 

            for j in range(i,10):
                temp.append(j)
                if sum(temp)<=n:
                    backtrack(j+1)
                temp.pop()

        backtrack(1)
        return ans

            

        
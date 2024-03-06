class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:


        ans=[]
        temp=[]
        def backtrack(i,s):
            if s==target:
                ans.append(list(temp))
                return 

            for j in range(i,len(candidates)):
                s+=candidates[j]
                temp.append(candidates[j])
                if s<=target:
                    backtrack(j,s)
                s-=candidates[j]
                temp.pop()

        backtrack(0,0)

        return ans

        
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final=[]
        def dfs(n,k):
            ans=[]
            def backtrack(start,l):
                if len(l)==k:
                    ans.append(l[::])
                    return
                for i in range(start,len(n)):
                    l.append(n[i])
                    backtrack(i+1,l)
                    l.pop()
            backtrack(0,[])
            return ans
        for i in range(len(nums)+1):
            final.extend(dfs(nums,i))
        return final
        
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust)==0 and n==1:
            return 1
        ans=[0]*(1+n)
        for i in trust:
            ans[i[0]]-=1
            ans[i[1]]+=1
        if n-1 in ans:
            return ans.index(n-1)
        else:
            return -1
            
            
                
            
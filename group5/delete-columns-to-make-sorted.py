class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        
        n=len(strs)
        m=len(strs[0])
        ans=0
        
        for j in range(m):
            for i in range(n-1):
                if strs[i+1][j]<strs[i][j]:
                    ans+=1
                    break
        return ans
        
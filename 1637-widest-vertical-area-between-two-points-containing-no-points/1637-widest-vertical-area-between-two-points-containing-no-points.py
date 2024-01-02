class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        ans=set()
        for x,y in points:
            ans.add(x)
        ans=list(ans)
        ans.sort()
        
        diff=0
        for i in range(len(ans)-1):
            
            diff=max(diff,ans[i+1]-ans[i])
        return diff
        
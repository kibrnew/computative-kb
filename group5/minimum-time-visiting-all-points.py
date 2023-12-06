class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        n=len(points)
        
        if n==1:
            return 1
        
        prev=points[0]
        ans=0
        for val in points[1:]:
            x=abs(val[0]-prev[0])
            y=abs(val[1]-prev[1])
            ans+=max(x,y)
            prev=val
        return ans
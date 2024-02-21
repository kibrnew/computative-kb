class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        
        ans=0
        right=-float("inf")
        for a,b in points:
            if a>right:
                ans+=1
                right=b
        return ans 
                
                
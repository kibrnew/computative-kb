class Solution:
    def maxArea(self, height: List[int]) -> int:
        pr1=0
        pr2=len(height)-1
        ans=0
        while pr1<pr2:
            ans=max(ans,min(height[pr1],height[pr2])*(pr2-pr1))
            if height[pr1]>height[pr2]:
                pr2-=1
            else:
                pr1+=1
        return ans 
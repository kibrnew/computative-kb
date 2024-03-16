class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:


        n=len(intervals)
        ans=[0]*(n)

        for i in range(n):
            intervals[i].append(i)

        intervals.sort()

        for start,end,i in intervals:
            cur=bisect_left(intervals,[end,end,0])
            if cur==n :
                ans[i]=-1
            else:
                ans[i]=intervals[cur][-1]
        return ans 


        
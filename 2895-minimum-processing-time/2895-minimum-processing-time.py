class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        pt=sorted(processorTime)
        n=len(pt)
        ans=0
        for i in range(n):
            ind=i*4
            ans=max(ans,max(tasks[ind:ind+4])+pt[i])
        return ans
            
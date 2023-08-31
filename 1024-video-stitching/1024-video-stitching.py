class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        start=0
        end=0
        n=len(clips)
        ans=0
        for i in range(n):
            for j in range(n):
                st,en=clips[j]
                if st<=start and en>end:
                    clips[i],clips[j]=clips[j],clips[i]
                    end=en
            ans+=1
            start=end
            if end>=time:
                return ans 
        
        return -1
       
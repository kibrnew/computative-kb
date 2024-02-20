class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        
        
        ans=0
        vis=set()
        for val in rolls:
            vis.add(val)
            if len(vis)==k:
                ans+=1
                vis=set()
        return ans+1 
        
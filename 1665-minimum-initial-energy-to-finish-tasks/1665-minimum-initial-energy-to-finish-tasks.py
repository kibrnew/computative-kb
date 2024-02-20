class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        
        ans=0
        for a,b in tasks:
            ans+=a
        tasks.sort(key=lambda x:x[0]-x[1])
        
        res=ans
        for a,b in tasks:
            if res<b:
                ans+=b-res
                res=b
            res-=a
        return ans 
       
        
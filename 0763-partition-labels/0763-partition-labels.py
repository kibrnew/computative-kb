class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ind={}
        n=len(s)
        for i in range(n):
            ind[s[i]]=i
            
        r=0
        ans=[]
        l=-1
        for i in range(n):
            val=s[i]
            r=max(r,ind[val])
            if r==i:
                ans.append(r-l)
                l=r
        return ans
            
    
            
                
            
                
            
            
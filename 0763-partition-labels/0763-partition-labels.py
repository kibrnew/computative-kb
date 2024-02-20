class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ind=defaultdict(list)
        n=len(s)
        for i in range(n):
            ind[s[i]].append(i)
            
        i=0
        r=0
        ans=[]
        l=-1
        while i<n:
            val=s[i]
            r=max(r,ind[val][-1])
            if r==i:
                ans.append(r-l)
                l=r
            i+=1
        return ans
            
    
            
                
            
                
            
            
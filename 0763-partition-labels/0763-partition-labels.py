class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cur=0
        ind=s.rfind(s[0])
        ans=[]
        last=-1
        while ind<len(s):
            ind=max(ind,s.rfind(s[cur]))
            while cur<ind:
                ind=max(ind,s.rfind(s[cur]))
                cur+=1
            ans.append(ind-last)
            last=ind
            ind+=1
            cur=ind
        return ans
    
            
                
            
                
            
            
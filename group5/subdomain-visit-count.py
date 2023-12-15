class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        count=defaultdict(int)
        
        for val in cpdomains:
            
            left,right=val.split(" ")
            
            c=int(left)
            
            count[right]+=c
            
            while "." in right:
                ind=right.index(".")
                right=right[ind+1:]
                count[right]+=c
                
        ans=[]      
        for key,val in count.items():
            ans.append(str(val)+" "+key)
            
        return ans
            
                
        
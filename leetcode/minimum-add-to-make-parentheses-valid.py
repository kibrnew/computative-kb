class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        ans=0
        count=Counter()
        for val in s:
            if val=="(":
                count[val]+=1
            else:
                if count["("]>0:
                    count["("]-=1
                else:
                    ans+=1
        ans+=count["("]
        return ans 
                    
        
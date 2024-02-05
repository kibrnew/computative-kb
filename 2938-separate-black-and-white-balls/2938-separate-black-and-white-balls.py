class Solution:
    def minimumSteps(self, s: str) -> int:
        
        n=len(s)
        count=0
        ans=0
        for val in s:
            if val=="0":
                ans+=count
            else:
                count+=1
        return ans
                
            
        
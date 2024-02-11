class Solution:
    def numberOfWays(self, s: str) -> int:
        ans=0
        l1=0
        l0=0
        r1=s.count("1")
        r0=s.count("0")
        
        for val in s:
            if val=="1":
                ans+=l0*r0
                l1+=1
                r1-=1
                
            else:
                ans+=l1*r1
                l0+=1
                r0-=1
        return ans
            

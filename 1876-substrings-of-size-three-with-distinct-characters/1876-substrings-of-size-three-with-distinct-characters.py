class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans=0
        if len(s)<3:
            return 0
        count=Counter([s[0],s[1],s[2]])
        if max(count.values())==1:
                ans+=1

        for i in range(3,len(s)):
            count[s[i-3]]-=1
            count[s[i]]+=1
            if max(count.values())==1:
                ans+=1
        return ans 
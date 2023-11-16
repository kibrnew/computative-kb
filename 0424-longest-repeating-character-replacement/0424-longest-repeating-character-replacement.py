class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n=len(s)
        ans=0
        key=set(s)
        for target in key:
            pr1=0
            temp=k
            for i, val in enumerate(s):
                if val!=target:
                    temp-=1
                if temp<0:
                    if s[pr1]!=target:
                        temp+=1
                    pr1+=1
            ans=max(ans,n-pr1)
            # print(ans)
        return ans


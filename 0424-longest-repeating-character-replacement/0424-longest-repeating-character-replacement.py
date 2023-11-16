class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=defaultdict(int)
        pr1=0
        n=len(s)
        maxi=0
        ans=0
        for i,val in enumerate(s):
            count[val]+=1
            maxi=max(maxi,count[val])
            if (i-pr1)-maxi>=k:
                count[s[pr1]]-=1
                pr1+=1  
            ans=max(ans,i-pr1+1)
        return ans 
                


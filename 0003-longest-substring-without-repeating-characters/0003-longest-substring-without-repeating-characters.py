class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count=defaultdict(int)
        n=len(s)
        pr1=0
        ans=0
        for i,val in enumerate(s):
            count[val]+=1
            while count[val]>1:
                cur=s[pr1]
                count[cur]-=1
                pr1+=1
            ans=max(ans,i-pr1+1)
        return ans
                
                
                
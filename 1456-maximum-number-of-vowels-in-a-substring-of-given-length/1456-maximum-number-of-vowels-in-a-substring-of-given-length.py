class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        pr1=0
        pr2=0
        store={'a','e','i','o','u'}
        ans=[]
        count=0
        for j in range(k):
            if s[j] in store:
                count+=1
        ans.append(count)
        for i in range(k,len(s)):
            if s[i] in store:
                count+=1
            if s[i-k] in store:
                count-=1
            ans.append(count)
            
        return max(ans)
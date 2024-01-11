class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        target=set("aeiou")
        count=0
        for val in s[:k]:
            if val in target:
                count+=1
        ans=count
        n=len(s)
        for i in range(n-k):
            if s[i] in target:
                count-=1
            if s[i+k] in target:
                count+=1
            ans=max(ans,count)
        return ans 
            
        
        
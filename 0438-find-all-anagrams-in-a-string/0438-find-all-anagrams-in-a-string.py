class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        k=len(p)
        target=Counter(p)
        count=Counter(s[:k])
        ans=[]
        n=len(s)
        
        if count==target:
            ans.append(0)
        
        for i in range(n-k):
            count[s[i]]-=1
            count[s[i+k]]+=1
            if count==target:
                ans.append(i+1)
                
        return ans
            
            
        
       
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        k=len(p)
        check=Counter(s[:k])
        target=Counter(p)
        n=len(s)
        ans=[]
        
        if check==target:
            ans.append(0)
        
        for i in range(n-k):
            check[s[i]]-=1
            check[s[i+k]]+=1
            if check==target:
                ans.append(i+1)
        return ans
            
                
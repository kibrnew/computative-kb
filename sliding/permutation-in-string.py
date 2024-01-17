class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n=len(s2)
        k=len(s1)
        
        if n<k:
            return False
        
        target=Counter(s1)
        count=Counter(s2[:k])
        if count==target:
            return True 
        
        for i in range(n-k):
            count[s2[i]]-=1
            count[s2[i+k]]+=1
            if count==target:
                return True
            # print(count)
            
        return False
            
        
        
        
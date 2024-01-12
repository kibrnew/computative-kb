class Solution:
    def balancedString(self, s: str) -> int:
        
        
        def check(a,b):
            for val in b:
                if a[val]<b[val]:
                    return False
            return True
                
    
        n=len(s)
        k=n//4
        count=Counter(s)
        target={}
        for key,val in count.items():
            if val>k:
                target[key]=val-k
                
        
        if not(target):
            return 0
        l=0
        cur=Counter()
        ans=n+1
    
        for r in range(n):
            cur[s[r]]+=1
            while check(cur,target):
                ans=min(ans,r-l+1)
                cur[s[l]]-=1
                l+=1
        return ans
                
                
            
        


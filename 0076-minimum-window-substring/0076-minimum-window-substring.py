class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
        def compare(a,b):
            for key in b:
                if a[key]<b[key]:
                    return False
            return True
        
        n=len(s)
        target=Counter(t)
        ans=(0,n+1)
        left=0
        count=Counter()
        
        for right in range(n):
            count[s[right]]+=1
            
            while compare(count,target):
                if right-left<ans[1]-ans[0]:
                    ans=(left,right)
                    # print("nsnsn")
                    
                count[s[left]]-=1
                left+=1
                # print("heere")
        
            # print(count)
        if ans[1]-ans[0]>n:
            return ""
        return s[ans[0]:ans[1]+1]
            
            
        
        
                
        
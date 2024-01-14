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
            
            if compare(count,target):
                while left<n and count[s[left]]>target[s[left]]:
        
                    count[s[left]]-=1
                    left+=1
                    
                if right-left<ans[1]-ans[0]:
                    ans=(left,right)


        if ans[1]-ans[0]>n:
            return ""
        return s[ans[0]:ans[1]+1]
            
            
        
        
                
        
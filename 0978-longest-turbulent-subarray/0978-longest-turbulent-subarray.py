class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n=len(arr)
        ans=2
        start=2
        flag=0
        for i in range(1,n-1):
            if arr[i-1]>=arr[i]>=arr[i+1] or arr[i-1]<=arr[i]<=arr[i+1]:
                ans=max(ans,start)
                start=2
              
            else :
                start+=1
        c=Counter(arr)
        if len(c)==1:
            return 1
        ans=max(ans,start)
        return ans 
                
        
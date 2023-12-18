class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        ans=list(s)
        n=len(s)
        ans[:k]=ans[k-1::-1]
        for i in range(2*k,n-2*k,2*k):
            ans[i:i+k]=ans[i+k-1:i-1:-1]
            # print(ans[i:i+k],)
        
        i=n%(2*k)
        # print(i,ans)
        if n>2*k:
            if i>k:
                ans[-i:-i+k]=ans[-1-i+k:-i-1:-1]
            else:
                ans[-i:]=ans[:-1-i:-1]
        return "".join(ans)
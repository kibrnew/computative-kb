class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        ans=[]
        n=len(s)
        flag=True
        # print(s[:15])
        
        for i in range(0,n,k):
            if flag:
                ans.append(s[i:i+k][::-1])
            else:
                ans.append(s[i:i+k])
            flag= not(flag)
        return "".join(ans)
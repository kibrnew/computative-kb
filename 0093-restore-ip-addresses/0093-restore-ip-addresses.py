class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans=[]
        def dfs(cur,remain):
            if len(cur)==4:
                if len(remain)==0:
                    ans.append(".".join(cur))
                return
            elif len(remain)==0:
                return 
            for i in range(1,4):
                new=cur+[remain[:i]]
                val=int(remain[:i])
                if val<256 and (i==1 or val>=10**(i-1)):
                    dfs(new,remain[i:])
        if len(s)>12:
            return []
        dfs([],s)
        return ans
            
                
            
        
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans=[]
        def dfs(cur,remain):
            if len(cur)==4:
                if len(remain)==0:
                    ans.append(".".join(cur))
                return
            maxum=9-3*len(cur)
            minum=3-len(cur)
            i=1
            while minum<=len(remain)-i:
                if maxum>=len(remain)-i:
                    new=cur+[remain[:i]]
                    val=int(remain[:i])
                    # print(i,val)
                    if val<256 and (i==1 or val>=10**(i-1)):
                        dfs(new,remain[i:])
                i+=1
        if len(s)>12:
            return []
        dfs([],s)
        return ans
            
                
            
        
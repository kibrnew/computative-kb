class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        n=len(s)
        stack=[]
        res=[]

        for i in range(n):
            val=s[i]
            if val=="(":
                stack.append(i)
            else:
                ind=stack.pop()
                cur=0
                while res and res[-1][0]>ind:
                    i,v=res.pop()
                    cur+=v

                if cur==0:
                    res.append((i,1))
                else:
                    res.append((i,cur*2))

        ans=0

        for i,v in res:
            ans+=v
        return ans 

        


        
class Solution:
    def decodeString(self, s: str) -> str:

        num=list("1234567890")

        

        
        def decoder(s):
            
            stack=[]
            n=len(s)
            res=[]
            for i in range(n):
                if s[i]=="[":
                    stack.append(i)
                elif s[i]=="]":
                    if len(stack)==1:
                        r=stack[0]
                        l=r-1
                        while s[l] in num:
                            l-=1

                        k=int(s[l+1:r])
                        res.append(decoder(s[r+1:i])*k)
                    stack.pop()
                else:
                    if not stack and s[i] not in num:
                        res.append(s[i])

            return "".join(res)

        return decoder(s)

        

            
            
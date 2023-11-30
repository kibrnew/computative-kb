class Solution:
    def interpret(self, command: str) -> str:
        ans=[]
        prev="ssd"
        for val in command:
            if val=="G":
                ans.append("G")
            elif val==")":
                if prev=="l":
                    ans.append("al")
                else:
                    ans.append("o")
            prev=val
        return "".join(ans)
            
        
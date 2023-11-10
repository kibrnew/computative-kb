class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        pr1=0
        m=len(s)
        if m==0:
            return True
        for val in t:
            if val==s[pr1]:
                pr1+=1
                if pr1==m:
                    return True 
        return False
        
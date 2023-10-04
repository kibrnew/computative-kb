class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        pr1=list(s)
        pr2=list(t)
        
        pr1.sort()
        pr2.sort()
        for i in range(len(pr1)):
            if not pr1[i]==pr2[i]:
                return pr2[i]
        return pr2[-1]
        
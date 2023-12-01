class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=[]
        n=len(word1)
        m=len(word2)
        for i in range(min(n,m)):
            s.append(word1[i])
            s.append(word2[i])
        i+=1
        if i!=n:
            s.append(word1[i:])
        if i!=m:
            s.append(word2[i:])
        return "".join(s)
        
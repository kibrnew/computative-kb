class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        k=list(set(list(s)))
        v=list(set(list(t)))
        if not(len(k)==len(v)):
            return False
        temp={s[i]:t[i] for i in range(len(s))}
        new=[]
        for i in s:
            new.append(temp[i])
        return t == "".join(new)
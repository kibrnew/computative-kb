class Solution:
    def romanToInt(self, s: str) -> int:
        changer={"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        roman=["I","V","X","L","C","D","M","P","q"]
        summ=0
        for i in range(len(s)-1):
            cur=s[i]
            ind=roman.index(cur)
            if roman[ind+1] ==s[i+1] or roman[ind+2]==s[i+1] :
                summ-=changer[cur]
            else:
                summ+=changer[cur]
        summ+=changer[s[-1]]
        return summ
class Solution:
    def sortSentence(self, s: str) -> str:
        sen = s.split(" ")
        sen2=[0]*len(sen)
        for i in sen:
            sen2[int(i[-1])-1]=i[:-1]
        sen3=" ".join(sen2)
        return sen3
        
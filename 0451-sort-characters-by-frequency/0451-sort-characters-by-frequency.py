class Solution:
    def frequencySort(self, s: str) -> str:
        j=list(s)
        count=Counter(j)
        new=count.keys()
        l=[]
        for val in new:
            l.append(val*count[val])
        l.sort(key=lambda x: len(x) )
        ans="".join(l[::-1])
        return ans
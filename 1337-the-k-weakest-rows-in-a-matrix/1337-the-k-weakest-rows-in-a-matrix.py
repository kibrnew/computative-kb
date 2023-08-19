class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        num=[]
        for i in mat:
            num.append(len(i)-bisect_left(i[::-1],1))
        print(num)
        d=defaultdict(list)
        for i in range(len(num)):
            d[num[i]].append(i)
        num.sort()
        ans=[]
        for i in range(k):
            ans.append(d[num[i]].pop(0))
        return ans
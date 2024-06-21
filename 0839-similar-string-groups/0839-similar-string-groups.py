class dsu:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
        self.size = [1 for i in range(size + 1)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px != py:
            if self.size[px] > self.size[py]:
                px, py = py, px
            self.parent[px] = py
            self.size[py] += self.size[px]

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def count(self):
        ans = 0
        for i in range(0,len(self.parent)-1):
            if i == self.parent[i]:
                ans += 1
        return ans

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
       
        n=len(strs)
        graph=dsu(n)
        for i in range(n):
            for j in range(i+1,n):
                count=0
                for k in range(len(strs[i])):
                    if strs[i][k]!=strs[j][k]:
                        count+=1
                if count<=2:
                    graph.union(i,j)

        return graph.count()

                
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        g={}
        for i in range(len(graph)):
            g[i]=graph[i]
        visited=set()
        color=defaultdict(int)
        ans=[]
        flag=[True]
        def dfs(node,c):
            for i in g[node]:
                if c==color[i]:
                    flag[0]=False
                    return 
                if i not in visited:
                    color[i]=-c
                    visited.add(i)
                    ans.append(i)
                    dfs(i,-c)
        for vertex in g.keys():
            if vertex not in visited:
                color[vertex]=1
                dfs(vertex,1)
        return flag[0]
        
        
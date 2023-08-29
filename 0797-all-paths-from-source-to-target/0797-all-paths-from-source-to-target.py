class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        g=defaultdict(list)
        for i in range(len(graph)):
            g[i]=graph[i]
        ans=[]
        def dfs(node,temp):
            temp.append(node)
            if node==len(graph)-1:
                ans.append(temp[::])
                temp.pop()
                return 
            for i in g[node]: 
                dfs(i,temp)
            temp.pop()
        dfs(0,[])
        return ans
        
            
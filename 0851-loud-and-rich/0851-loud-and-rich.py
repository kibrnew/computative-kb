class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n=len(quiet)
        graph=defaultdict(list)
        for a,b in richer:
            graph[b].append(a)
        def dfs(node):
            visited.add(node)
            if quiet[node]<quiet[ans[0]]:
                ans[0]=node
                
            for i in graph[node]:
                if i not in visited:
                    dfs(i)
        final=[]
        for i in range(n):
            ans=[i]
            visited=set()
            dfs(i)
            final.append(ans[0])
        
        
        return final
        
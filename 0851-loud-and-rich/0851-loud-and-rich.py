class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n=len(quiet)
        graph=defaultdict(list)
        for a,b in richer:
            graph[b].append(a)
        ans={}
        visited=set()
        def dfs(node):
            visited.add(node)
            val=[node]
            for i in graph[node]:
                if i not in ans:
                    val.append(dfs(i))
                else:
                    val.append(ans[i])
            small=node
            for j in val:
                if quiet[j]<quiet[small]:
                    small=j
            ans[node]=small
            return small
        final=[]
        for i in range(n):
            if i not in visited:
                dfs(i)
            final.append(ans[i])
        
        return final
        
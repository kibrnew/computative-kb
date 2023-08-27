class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(list)
        weight={}
        for i,(a,b) in enumerate(equations):
            graph[a].append(b)
            graph[b].append(a)
            weight[(a,b)]=values[i]
            weight[(b,a)]=1/values[i]
        def dfs(node,target,count):
            visited.add(node)
            if not graph[node]:
                return -1
            if node==target:
                return count
            for i in graph[node]:
                if i not in visited:
                    ans=dfs(i,target,count*weight[(node,i)])
                    if ans !=-1:
                        return ans
            return -1
        ans=[]
        for start,end in queries:
            visited=set()
            ans.append(dfs(start,end,1))
        return ans

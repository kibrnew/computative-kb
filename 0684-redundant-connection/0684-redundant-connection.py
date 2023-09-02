class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph=defaultdict(set)
        def dfs(node,target):
            if node not in visited:
                visited.add(node)
                if node==target:
                    return True 
                for child in graph[node]:
                    if dfs(child,target):
                        return True 
        for start,end in edges:
            visited=set()
            if graph[start] and graph[end] and dfs(start,end):
                return start,end
            graph[start].add(end)
            graph[end].add(start)
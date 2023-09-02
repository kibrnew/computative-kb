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
        for root,edge in edges:
            visited=set()
            if root in graph and edge in graph and dfs(root,edge):
                return root,edge
            graph[root].add(edge)
            graph[edge].add(root)
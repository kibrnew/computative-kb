class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        for a,b in edges:
            if graph[a]:
                graph[a].append(b)
            else:
                graph[a]=[b]
            if graph[b]:
                graph[b].append(a)
            else:
                graph[b]=[a]
            
        print(graph)
        for ind in graph.keys():
            if len(graph[ind]) == len(edges):
                return ind
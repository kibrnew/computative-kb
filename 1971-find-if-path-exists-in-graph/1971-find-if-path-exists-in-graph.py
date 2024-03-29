class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
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
        visited=set([source])
        queue=deque([source])
        while queue:
            temp=queue.popleft()
            if temp==destination:
                return True 
            for vertex in graph[temp]:
                if vertex not in visited:
                    visited.add(vertex)
                    queue.append(vertex)       
        return False
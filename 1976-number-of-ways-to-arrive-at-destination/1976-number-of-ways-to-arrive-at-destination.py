class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        graph=defaultdict(list)
        cost={}
        for a,b,c in roads:
            graph[a].append(b)
            graph[b].append(a)
            cost[(a,b)]=c
            cost[(b,a)]=c
        
        def dj(graph,cost,start):
            distances={node:float("inf") for node in graph}
            paths={node:0 for node in graph}
            distances[start]=0
            paths[start]=1
            visited=set()
            heap=[]
            heappush(heap,(0,start))
            mini=float("inf")
            ans="inf"
            while heap:
                dist,parent=heappop(heap)
                if parent in visited:
                    continue
                visited.add(parent)
                for child in graph[parent]:
                    temp=dist+cost[(parent,child)]
                    if temp<distances[child]:
                        distances[child]=temp
                        paths[child]=paths[parent]
                        heappush(heap,(temp,child))
                    elif temp==distances[child]:
                        paths[child]=(paths[child]+paths[parent])% 1_000_000_007
            return paths[n-1]
        return dj(graph,cost,0)
            
            
        
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append([v, time])
            graph[v].append([u, time])

        def dijkstra(src):
            dist = [math.inf] * n
            ways = [0] * n
            minHeap = [(0, src)]  # dist, src
            dist[src] = 0
            ways[src] = 1
            while minHeap:
                d, u = heappop(minHeap)
                if dist[u] < d: continue  # Skip if `d` is not updated to latest version!
                for v, time in graph[u]:
                    if dist[v] > d + time:
                        dist[v] = d + time
                        ways[v] = ways[u]
                        heappush(minHeap, (dist[v], v))
                    elif dist[v] == d + time:
                        ways[v] = (ways[v] + ways[u]) % 1_000_000_007
            return ways[n - 1]

        return dijkstra(0)

# class Solution:
#     def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
#         graph=defaultdict(list)
#         cost={}
#         for a,b,c in roads:
#             graph[a].append(b)
#             graph[b].append(a)
#             cost[(a,b)]=c
#             cost[(b,a)]=c
        
#         def dj(graph,cost,start):
#             distances={node:float("inf") for node in graph}
#             paths={node:0 for node in graph}
#             distances[start]=0
#             paths[start]=1
#             visited=set()
#             heap=[]
#             heappush(heap,(0,start))
#             mini=float("inf")
#             ans="inf"
#             while heap:
#                 dist,parent=heappop(heap)
#                 if parent in visited:
#                     continue
#                 visited.add(parent)
#                 for child in graph[parent]:
#                     temp=dist+cost[(parent,child)]
#                     if temp<=distances[child]:
#                         distances[child]=temp
#                         paths[child]+=paths[parent]
#                         heappush(heap,(temp,child))
#             return paths[n-1]
#         return dj(graph,cost,0)
            
            
        
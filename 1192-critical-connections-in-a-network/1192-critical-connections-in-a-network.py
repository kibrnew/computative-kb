class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        graph=defaultdict(list)
        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)

        vis=[0]*n
        ans=[]

        def dfs(node,level,p):

            vis[node]=level
            mini=level
            for child in graph[node]:
                if vis[child]==0:
                    cur=dfs(child,level+1,node)
                    if cur>level:
                        ans.append((node,child))
                    mini=min(cur,mini)

                else:
                    if child!=p:
                        mini=min(mini,vis[child])


            return mini


        dfs(0,1,-1)

        return ans

            

        
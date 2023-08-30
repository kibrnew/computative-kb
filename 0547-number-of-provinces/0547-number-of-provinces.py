class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        count=0
        stor=[i for i in range(n)]
        visited=[False]*n
        while len(stor)>0:
            count+=1
            queue=deque()
            queue.append(stor[0])
            visited[stor[0]]=True
            stor.pop(0)
            while queue:
                vertex=queue.pop()
                for i in range(n):
                    if isConnected[vertex][i]==1 and not visited[i]:
                        queue.append(i)
                        visited[i]=True
                        stor.remove(i)
        return count
        
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited=set()
        graph=defaultdict(list)
        for i in prerequisites:
            graph[i[0]].append(i[1])
        visited=set()
        def dfs(node):
            if node in visited:
                print("here")
                return False
            if graph[node]==[]:
                return True
            visited.add(node)
            for pre in graph[node]:
                if not dfs(pre):
                    return False
            visited.remove(node)
            graph[node]=[]
            return True
        print(graph)
        for keys in range(numCourses):
            if not dfs(keys):
                return False
        return True
            
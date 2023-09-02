class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set([0])
        def dfs(node):
            visited.add(node)
            for temp in rooms[node]:
                if temp not in visited:
                    dfs(temp)
        dfs(0)
        for i in range(len(rooms)):
            if i not in visited:
                return False
        return True
       
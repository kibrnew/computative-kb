class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, x, y):
            root_x = find(parent, x)
            root_y = find(parent, y)
            if root_x != root_y:
                parent[root_x] = root_y

        n = len(edges)
        parent = list(range(n + 1))  # Create a parent list to represent disjoint sets

        for edge in edges:
            u, v = edge
            if find(parent, u) == find(parent, v):
                return edge
            else:
                union(parent, u, v)

        return []  # Return an empty list if no redundant edge is found

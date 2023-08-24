"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph={}
        importance={}
        for i in employees:
            graph[i.id]=i.subordinates
            importance[i.id]=i.importance
        def dfs(node):
            ans=importance[node]
            for i in graph[node]:
                ans+=dfs(i)
            return ans
                
        return dfs(id)
        
                    
                
        
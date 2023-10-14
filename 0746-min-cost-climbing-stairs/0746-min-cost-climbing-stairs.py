class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost=[0]+cost
        @cache
        def dfs(i):
            if i>=len(cost):
                return 0
            return  min(dfs(i+1),dfs(i+2))+cost[i]
        return dfs(0)
        
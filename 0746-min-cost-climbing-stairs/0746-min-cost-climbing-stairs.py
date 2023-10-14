class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost=[0]+cost
        dp={}
        def dfs(i):
            if i>=len(cost):
                return 0
            if i in dp:
                return dp[i]
            dp[i]=min(dfs(i+1),dfs(i+2))+cost[i]
            return dp[i]
        return dfs(0)
        
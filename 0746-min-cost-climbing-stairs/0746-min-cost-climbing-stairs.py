class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost=[0]+cost
        dp=[0]*len(cost)
        def dfs(i):
            if i>=len(cost):
                return 0
            if dp[i]!=0:
                return dp[i]
            dp[i]=min(dfs(i+1),dfs(i+2))+cost[i]
            return dp[i]
        # dp=[0]*(len(cost))
        # for i in reversed(range(i)):
        #     dp[i]=min(dfs(i))
            
        return dfs(0)
    
    
        
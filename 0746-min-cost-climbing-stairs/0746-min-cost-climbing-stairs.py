class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        c = {n:0,n-1:cost[n-1]}
        def min_cost(k):
            if k in c:
                return c[k]
            c[k] = cost[k] + min(min_cost(k+1),min_cost(k+2))
            return c[k]

        return min(min_cost(1),min_cost(0))
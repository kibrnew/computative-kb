class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366

        for j, idx in enumerate(days):
            if j > 0:
                for i in range(days[j-1]+1, days[j]):
                    dp[i] = dp[i-1]

            dp[idx] =  min(dp[idx - 1] + costs[0], dp[max(idx - 7, 0)] + costs[1], dp[max(idx - 30, 0)] + costs[2])

        return dp[days[-1]]
            


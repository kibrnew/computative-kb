class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        dp=[float("inf")]*(n+1)
        dp[src]=0
        for _ in range(k+1):
            temp=dp[:]
            for start,end,price in flights:
                temp[end]=min(dp[start]+price, temp[end])

            dp=temp
        print(dp)
        if dp[dst]==float("inf"):
            return -1
        return dp[dst]



        
class Solution:
    def canCross(self, stones: List[int]) -> bool:

        dp=[{0}]
        
        for i in range(1,len(stones)):
            dp.append(set())
            for j in range(i):
                diff=stones[i]-stones[j]

                if diff in dp[j] or diff+1 in dp[j] or diff-1 in dp[j]:
                    dp[-1].add(diff)

        return dp[-1]
        
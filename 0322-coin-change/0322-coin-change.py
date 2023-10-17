class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        @cache
        def dp(s):
            if s > amount:
                return float('inf')

            if s == amount:
                return 0
                
            mini = float('inf')
            for idx in range(len(coins)):
                mini = min(dp(s + coins[idx])+ 1, mini) 
            
            return mini 

        ans = dp(0)  
        return ans if ans != float('inf') else -1
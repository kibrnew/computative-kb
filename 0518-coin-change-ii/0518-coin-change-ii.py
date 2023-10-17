class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @cache
        def dp(s,i):
            
            if s > amount:
                return 0
            if i>=len(coins):
                return 0

            if s == amount:
                return 1
                
            mini = dp(s + coins[i],i)+dp(s,i+1)
            
            return mini 


        return dp(0,0)  
  
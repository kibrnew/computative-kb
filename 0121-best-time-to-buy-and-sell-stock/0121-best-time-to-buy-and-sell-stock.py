class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        n=len(prices)
        buy=prices[0]
        for val in prices:
            ans=max(ans,val-buy)
            buy=min(val,buy)
        # print(ans)
        return ans
            
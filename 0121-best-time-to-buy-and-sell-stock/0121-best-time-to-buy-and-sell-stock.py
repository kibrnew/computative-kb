class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pr1=0
        pr2=1
        ans=0
        while pr2<len(prices):
            if prices[pr1]>prices[pr2]:
                pr1=pr2
            ans=max(ans,prices[pr2]-prices[pr1])  
            pr2+=1
        return ans
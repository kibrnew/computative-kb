class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n=len(piles)
        
        new=piles[n//3:]
        ans=0
        for i in range(len(new)):
            if i%2==0:
                ans+=new[i]
        return ans
            

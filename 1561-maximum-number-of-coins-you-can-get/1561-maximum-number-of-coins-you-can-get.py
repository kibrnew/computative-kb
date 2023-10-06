class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans=0
        for i in range(len(piles)//3):
            # print(piles[-2*i-2])
            ans += piles[-2*i-2]
        return ans

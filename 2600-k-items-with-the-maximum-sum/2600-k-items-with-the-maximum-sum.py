class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans=min(numOnes,k)
        k-=min(numOnes,k)
        if k:
            k-=min(numZeros,k)
        if k:
            ans-=min(numNegOnes,k)
        return ans
            
            
            
            
        
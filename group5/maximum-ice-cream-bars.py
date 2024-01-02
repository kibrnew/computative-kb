class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans=0
        for val in costs:
            coins-=val
            if coins<0:
                break
            else:
                ans+=1
        return ans
                
        
        
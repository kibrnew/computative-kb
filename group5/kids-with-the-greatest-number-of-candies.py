class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        maxi=max(candies)
        
        for candy in candies:
            ans.append(candy+extraCandies>=maxi)
            
        return ans 
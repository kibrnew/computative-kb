class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        ans=0
        cur=capacity
        for i,val in enumerate(plants):

            if val>cur:
                ans+=2*i
                cur=capacity
            ans+=1
            cur-=val
        return ans
                
        
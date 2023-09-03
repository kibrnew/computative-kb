class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        n=len(heaters)-1
        ans=0
        for house in houses:
            ind=bisect_left(heaters,house)
            if ind==0 :
                ans=max(ans,abs(house-heaters[ind]))
            elif ind<=n:
                    right=abs(house-heaters[ind-1])
                    left=abs(house-heaters[ind])
                    ans=max(ans,min(left,right))
            else:
                ans=max(ans,abs(heaters[-1]-house))
                    
                
        return ans
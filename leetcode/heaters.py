class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        houses.sort()
        heaters.sort()
        ans=0

        for val in houses:
            ind=bisect_left(heaters,val)
            if ind==len(heaters):
                ans=max(ans,val-heaters[-1])
            else:
                cur=abs(val-heaters[ind])
                if ind+1<len(heaters):
                    cur=min(cur,abs(val-heaters[ind+1]))
                    
                if ind-1>=0:
                    cur=min(cur,abs(val-heaters[ind-1]))

                ans=max(ans,cur)

        return ans 


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        houses.sort()
        heaters.sort()
        r=max(houses+heaters)
        heaters.append(10**10)
        

        def calc(t):
            for val in houses:
                ind=bisect_left(heaters,val)
                if abs(val-heaters[ind])<=t:
                    continue
                if abs(val-heaters[ind-1])<=t:
                    continue 
                return False
                

            return True 



        l=0
      

        while l<=r:
            mid=(l+r)//2
            
            if calc(mid):
                r=mid-1
            else:
                l=mid+1

        return l


        
        # return 1
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        temp=[0]*(n+1)
        
        for l,r,val in bookings:
            temp[l-1]+=val
            temp[r]-=val
        
        for i in range(1,n):
            temp[i]+=temp[i-1]
        return temp[:-1]
            
            
        
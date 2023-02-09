class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0]*(n+1)
        
        for book in bookings:
            prefix[book[0]-1]+=book[2]
            prefix[book[1]]-=book[2]
        tot = 0
        for i,pre in enumerate(prefix):
            tot+=pre
            prefix[i]=tot
        
        return prefix[0:n]
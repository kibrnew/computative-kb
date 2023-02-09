class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        #time_complexity = o(n)
        #space complexity = o(n)
        
        #intialize a list to perform prefix sum on the intervals
        prefix = [0]*(n+1)
        
        #iterate to each book and assign to their correspondence interval
        for book in bookings:
            prefix[book[0]-1]+=book[2]
            prefix[book[1]]-=book[2]
        
        #apply prefix sum on the assigned interval to get the total sum on each interval
        tot = 0
        for i,pre in enumerate(prefix):
            tot+=pre
            prefix[i]=tot
            
        #return the answer upto n 
        return prefix[0:n]
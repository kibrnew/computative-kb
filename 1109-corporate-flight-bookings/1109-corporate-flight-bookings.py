class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * (n + 1)

        # iterate over each booking and assign it to its corresponding interval
        for booking in bookings:
            start, end, seats = booking
            prefix[start - 1] += seats
            prefix[end] -= seats

        # apply prefix sum on the assigned interval to get the total sum on each interval
        total_seats = 0
        for i in range(n + 1):
            total_seats += prefix[i]
            prefix[i] = total_seats

        # return the answer up to n
        return prefix[:n]
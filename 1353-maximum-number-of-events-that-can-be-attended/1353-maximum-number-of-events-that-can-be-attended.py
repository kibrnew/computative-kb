class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(reverse=True)
        temp= []
        ans= d = 0
        while events or temp:
            if not temp: d = events[-1][0]
            while events and events[-1][0] <= d:
                heapq.heappush(temp, events.pop()[1])
            heapq.heappop(temp)
            ans+= 1
            d += 1
            while temp and temp[0] < d:
                heapq.heappop(temp)
        return ans
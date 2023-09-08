class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(reverse=True)
        heap= []
        ans= cur = 0
        while events or heap:
            if not heap:
                cur= events[-1][0]
            while events and events[-1][0] <= cur:
                heappush(heap, events.pop()[1])
            heappop(heap)
            ans+= 1
            cur += 1
            while heap and heap[0] < cur:
                heappop(heap)
        return ans
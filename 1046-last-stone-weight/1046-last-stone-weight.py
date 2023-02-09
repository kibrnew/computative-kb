class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        stone=[-i for i in stones]
        heapq.heapify(stone) 
        while len(stone)>1:
            y=heappop(stone)
            x=heappop(stone)
            if x>y:
                y=y-x
                heappush(stone, y)
        if not stone:
            return 0
        ans=-heappop(stone)
        return ans
                
        
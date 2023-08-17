class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new=[-i for i in stones]
        stones[:]=new[:]
        heapify(stones)
        while len(stones)>1:
            y=heappop(stones)
            x=heappop(stones)
            if x==y:
                continue
            else:
                heappush(stones,y-x)
        if not stones:
            return 0
        else:
            return -stones[0]
        
            
        
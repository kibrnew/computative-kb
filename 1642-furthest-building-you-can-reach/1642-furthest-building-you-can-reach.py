class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        temp=[]
        n=len(heights)
        for i in range(n-1):
            temp.append(heights[i+1]-heights[i])
        use=[]
        heapify(use)
        for j,i in enumerate (temp):
            if i>0:
                if i<=bricks:
                    heappush(use,-i)
                    bricks-=i
                elif ladders>0:
                    if use:
                        p=-heappop(use)
                        d=p-i
                        if d>0:
                            bricks+=d
                            heappush(use,-i)
                        else:
                            heappush(use,-p)
                    ladders-=1
                else:
                    return j
        return n-1
                    
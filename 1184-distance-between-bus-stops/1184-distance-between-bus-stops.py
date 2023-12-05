class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:    
        n=len(distance)
        # distance=distance+distance
        first=min(start,destination)
        last=max(start,destination)
        
        ans1=0
        ans2=0
        for i in range(first,n+first):
            ind=i%n
            if i<last:
                ans1+=distance[i]
            elif i<start+n:
                ans2+=distance[ind]
        return min(ans1,ans2)
                
        
        # return min(sum(distance[last:first+n]),sum(distance[first:last]))
        
        
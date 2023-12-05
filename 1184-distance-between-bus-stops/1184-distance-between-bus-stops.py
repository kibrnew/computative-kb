class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:    
        n=len(distance)
        distance=distance+distance
        first=min(start,destination)
        last=max(start,destination)
        
        return min(sum(distance[last:first+n]),sum(distance[first:last]))
        
        
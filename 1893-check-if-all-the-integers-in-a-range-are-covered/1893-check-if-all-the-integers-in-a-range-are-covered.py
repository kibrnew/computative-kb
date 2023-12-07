class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        ans=set()
        
        for start,end in ranges:
            ans|=set(range(start,end+1))
            
            
        return all(val in ans for val in range(left,right+1) )
            
        
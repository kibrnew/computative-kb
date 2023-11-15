class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        last=max(trips,key=lambda x:x[-1])[-1]
        
        prefix=[0]*(last+1)
        
        for np,start,end in trips:
            prefix[start]+=np
            prefix[end]-=np
        s=0
        for val in prefix:
            s+=val
            if s>capacity:
                return False
        return True
        
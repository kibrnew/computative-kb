class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        maxi=max(trips,key=lambda x:x[-1])[-1]
        ans=[0]*(maxi+1)
        
        for val,left,right in trips:
            ans[left]+=val
            ans[right]-=val
        
        s=0
        for val in ans:
            s+=val
            if s>capacity :
                return False
        return True 
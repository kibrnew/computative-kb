class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        l=len(requests)
        ans=0
        temp=[0]*n
        
        def track(ind,count):
            print(ind)
            if ind==l:
                if all (x==0 for x in temp):
                    nonlocal ans
                    ans=max(ans,count)
                return 
            track (ind+1,count)
            start,end=requests[ind]
            temp[start]-=1
            temp[end]+=1
            track(ind+1,count+1)
            temp[end]-=1
            temp[start]+=1
            
        track(0,0)
        return ans 
        
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d=defaultdict(bool)
        temp=[]
        for i in range(len(points)):
            w=((points[i][0])**2)+((points[i][1])**2)
            temp.append(w)
            if not d[w]:
                d[w]=[points[i]]
            else :
                d[w].append(points[i])
        temp.sort()
        ans=[]
        for j in range(k):
            ind=d[temp[j]].pop()
            ans.append(ind)
            
        return ans
            
            
        
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        temp=[]
        for i in range(len(points)):
            w=((points[i][0])**2)+((points[i][1])**2)
            temp.append((w,i))
        print(temp)
        temp.sort()
        ans=[]
        for j in range(k):
            ind=temp[j][1]
            ans.append(points[ind])
        return ans
            
            
        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n=len(matrix)
        m=len(matrix[0])

        l=0
        r=n-1
        while l<=r:
            mid=(l+r)//2
            if matrix[mid][0]<=target:
                l=mid+1
            else:
                r=mid-1
        cur=r
        # print(cur)
        if cur>=0:
            l=0
            r=m-1
            while l<=r:
                mid=(l+r)//2
                if matrix[cur][mid]==target:
                    return True 
                elif matrix[cur][mid]<target:
                    l=mid+1
                else:
                    r=mid-1
        
        return False
        


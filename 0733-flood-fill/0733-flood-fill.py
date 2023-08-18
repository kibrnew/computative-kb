class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited=set([(sr,sc)])
        queue=deque([[sr,sc]])
        cur=image[sr][sc]
        while queue:
            m,n=queue.popleft()
            if m>0 and image[m-1][n]==cur and ((m-1,n) not in visited):
                visited.add((m-1,n))
                queue.append([m-1,n])
                image[m-1][n]=color
            if m<len(image)-1 and image[m+1][n]==cur and ((m+1,n) not in visited):
                visited.add((m+1,n))
                queue.append([m+1,n])
                image[m+1][n]=color
            if n>0 and image[m][n-1]==cur and ((m,n-1) not in visited):
                visited.add((m,n-1))
                queue.append((m,n-1))
                image[m][n-1]=color
            if n<len(image[0])-1 and image[m][n+1]==cur and ((m,n+1) not in visited):
                visited.add((m,n+1))
                queue.append((m,n+1))
                image[m][n+1]=color
        image[sr][sc]=color
        return image
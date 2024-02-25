class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        
        stack=[]
        n=len(temp)
        ans=[0]*(n)
        
        for i in range(n):
            while stack and temp[stack[-1]]<temp[i]:
                ind=stack.pop()
                ans[ind]=i-ind
                
            stack.append(i)
            
        return ans 
                
            
      
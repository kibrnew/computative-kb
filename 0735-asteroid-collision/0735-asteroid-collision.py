class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans=[]
        for i in asteroids:
            if not ans or ans[-1]<0 or i>0:
                ans.append(i)
            else :
                f=0
                while ans:
                    if ans[-1]==abs(i):
                        ans.pop()
                        f=1
                        break
                    elif ans[-1]>abs(i):
                        break 
                    elif ans[-1]<0:
                        ans.append(i)
                        break
                    else:
                        ans.pop()
                if not ans and f==0:
                    ans.append(i)
        return ans 
                    
            
            
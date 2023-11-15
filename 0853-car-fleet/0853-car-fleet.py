class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        temp=sorted(zip(position,speed),reverse=True)
        maxi=0
        ans=0
        # print(temp)
        for pos,speed in temp:
            t=(target-pos)/speed
            if t>maxi:
                ans+=1
                maxi=t
        return ans
                
            
            
      
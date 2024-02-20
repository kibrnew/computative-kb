class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans=0
        n=len(costs)//2
        costs.sort(key=lambda x:(-abs(x[0]-x[1])))
        
        i=0
        j=0
        for a,b in costs:
            if j==n:
                ans+=a
            elif i==n:
                ans+=b
            else:
                if a<b:
                    ans+=a
                    i+=1
                elif b<a:
                    ans+=b
                    j+=1
                else:
                    ans+=a
        return ans
                
            
        
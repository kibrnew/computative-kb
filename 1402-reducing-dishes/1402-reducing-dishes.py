class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        s=0
        for i in range(len(satisfaction)):
            s+=satisfaction[i]*(i+1)
        val=satisfaction.pop(0)
        while val<0:
            s2=0
            for i in range(len(satisfaction)):
                s2+=satisfaction[i]*(i+1)
            s=max(s,s2)
            if len(satisfaction)==0:
                return 0
            val=satisfaction.pop(0)
        return s
                
    
            
        
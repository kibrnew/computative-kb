class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        
        ans= [] 
        if finalSum%2:
            return ans
    
        c = 2
        
        while finalSum >= 2*c+2:
            finalSum -= c 

            ans.append(c)
            c+=2
            
        if finalSum:
            ans.append(finalSum)
        return ans


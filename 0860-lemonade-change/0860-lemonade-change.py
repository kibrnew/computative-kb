class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        count=Counter()
        for val in bills:
            count[val]+=1
            if val==10:
                if count[5]==0:
                    return False 
                count[5]-=1
            if val==20:
                f=False
                if count[10]>0:
                    count[10]-=1
                    val-=10
                if val==10:
                    if count[5]==0:
                        return False
                    count[5]-=1
                else:
                    if count[5]<3:
                        return False
                    count[5]-=3
            
        return True 
            
        
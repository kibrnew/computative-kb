class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        pr1=0
        count=0
        f1=0
        f2=0
        type2=type1=fruits[0]
        ans=set([])
        for i in range(len(fruits)):
            if fruits[i]==type1 :
                f1+=1
                f2=0
                count+=1
            elif fruits[i]==type2:
                f2+=1
                f1=0
                count+=1
            else:
                if f1==0:
                    f1=1
                    count=f2+f1
                    f2=0
                    type1=fruits[i]
                else:
                    f2=1
                    count=f2+f1
                    f1=0
                    type2=fruits[i]
            ans.add(count)
        return max(ans)
                    
                    
                    
            
            
            
        
        
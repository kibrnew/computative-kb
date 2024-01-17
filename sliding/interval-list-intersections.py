class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        n=len(firstList)
        m=len(secondList)
        i=0
        j=0
        ans=[]
        while i<n and j<m:
            a,b=firstList[i]
            c,d=secondList[j]
            
            if c<=a<=d:
                if c<=b<=d:
                    ans.append([a,b])
                    i+=1
                else:
                    ans.append([a,d])
                    j+=1
                    
            elif a<=c<=b:
                if a<=d<=b:
                    ans.append([c,d])
                    j+=1
                else:
                    ans.append([c,b])
                    i+=1
            else:
                if a>c:
                    j+=1
                else:
                    i+=1
        return ans
                    
                
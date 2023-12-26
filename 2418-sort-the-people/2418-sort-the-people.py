class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
#         n= len(names)
        
#         for i in range(n):
#             for j in range(i+1,n):
                
#                 if heights[i]<heights[j]:
#                     heights[i],heights[j]=heights[j],heights[i]
#                     names[i],names[j]=names[j],names[i]
                    
#         return names
        new=sorted(zip(heights,names),reverse=True)
        ans=[]
        for h,n in new:
            ans.append(n)
        return ans 
    
    
                    
            
      
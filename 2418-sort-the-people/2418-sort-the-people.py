class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        
        place=[0]*(max(heights)+1)
        
        for i in range(len(names)):
            place[heights[i]]=names[i]
            
        ans=[]
        
        for val in place[::-1]:
            if val:
                ans.append(val)
        return ans
            
        
        
# insertion sort 
        
#         n=len(names)
        
#         for i in range(1,n):
#             for j in range(i,0,-1):
#                 if heights[j]>heights[j-1]:
#                     heights[j], heights[j-1]= heights[j-1], heights[j]
#                     names[j-1],names[j]=names[j],names[j-1]
#                 else:
#                     break
#         return names
                    
        
        
        # bubble sort 
        
#         n= len(names)
        
#         for i in range(n-1):
#             flag=True
#             for j in range(n-i-1):
#                 if heights[j]<heights[j+1]:
#                     heights[j], heights[j+1]= heights[j+1], heights[j]
#                     names[j+1],names[j]=names[j],names[j+1]
#                     flag=False
#             if flag:
#                 break
#         return names
        
   # selection sort
        
#         n= len(names)
        
#         for i in range(n):
#             for j in range(i+1,n):
                
#                 if heights[i]<heights[j]:
#                     heights[i],heights[j]=heights[j],heights[i]
#                     names[i],names[j]=names[j],names[i]
                    
#         return names


# the healthy way
        # new=sorted(zip(heights,names),reverse=True)
        # ans=[]
        # for h,n in new:
        #     ans.append(n)
        # return ans 
        
        
    
    
                    
            
      
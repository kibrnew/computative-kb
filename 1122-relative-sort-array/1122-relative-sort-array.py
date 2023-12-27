class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
            
        
        n=len(arr1)
        m=len(arr2)
        check=set(arr2)
        ind={}
        for i,val in enumerate(arr2):
            ind[val]=i
        
        def sorter(x):
            if x in check:
                return ind[x]
            else:
                return (x+999)
        arr1.sort(key=sorter)
        return arr1
            
        
#         ind={}
#         for i,val in enumerate(arr2):
#             ind[val]=i
            
#         temp=[]
#         count=[0]*m
#         for val in arr1:
#             if val in ind:
#                 count[ind[val]]+=1
#             else:
#                 count.append(val)
        
#         ans=[]
#         for i in range(m):
#             ans.extend()
            
            
      
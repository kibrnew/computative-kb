class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
            
        ind={}
        
        for i,val in enumerate(arr2):
            ind[val]=i
        
        def sorter(x):
            if x in ind:
                return ind[x]
            else:
                return (x+1000)
            
        arr1.sort(key=sorter)
        return arr1

            
            
      
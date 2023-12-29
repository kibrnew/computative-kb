class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        n=len(arr)
        ans=[]
        for i in range(n,0,-1):
            ind=arr.index(max(arr[:i]))+1
            ans.append(ind)
            ans.append(i)
            arr[:ind]=arr[:ind][::-1]
            arr[:i]=arr[:i][::-1]
        return ans
            
        
            
            
            
            
        
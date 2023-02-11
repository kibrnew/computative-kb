class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        for i in range(len(arr)-1,-1,-1):
            ind=arr.index(max(arr[:i+1]))
            if ind==i:
                continue 
            arr[ind::-1]=arr[:ind+1]
            arr[:i+1]=arr[i::-1]
            ans.append(ind+1)
            ans.append(i+1)
        return ans
            
            
            
            
        
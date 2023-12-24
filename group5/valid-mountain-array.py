class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        k=len(arr) 
        flag=0
        if k<3:
            return False
        elif arr[0]>arr[1]:
            return False
        
        for i in range(1,k):
            
            if arr[i-1] == arr[i]:
                return False
            
            if flag==0:
                if arr[i-1]>arr[i]:
                    flag=1
                    
            if flag==1:
                if arr[i-1]<arr[i]:
                    return False 
                
        if flag==0:
            return False 
        return True 

        
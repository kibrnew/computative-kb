class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pr1=0
        pr2=k
        
        while pr2<len(arr):
            left=abs(arr[pr1]-x)
            right=abs(arr[pr2]-x)
            if right<left:
                pr1+=1
                pr2+=1
            else:
                if arr[pr1]!=arr[pr2]:
                    break
                else:
                    pr2+=1
                    pr1+=1
        return arr[pr1:pr2]
        
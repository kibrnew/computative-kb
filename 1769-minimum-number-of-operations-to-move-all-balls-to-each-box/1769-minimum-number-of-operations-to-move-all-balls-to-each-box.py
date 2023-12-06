class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        n=len(boxes)
        ans=[]
        
        for i in range(n):
            temp=0
            
            for j in range(n):
                if boxes[j]=="1":
                    temp+=abs(j-i)
            ans.append(temp)
        return ans
        
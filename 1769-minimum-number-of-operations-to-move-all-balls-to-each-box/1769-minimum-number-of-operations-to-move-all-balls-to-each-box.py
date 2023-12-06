class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        n=len(boxes)
        ans=[]
        
        ind=[]
        for i in range(n):
            if boxes[i]=="1":
                ind.append(i)
        
        for i in range(n):
            temp=0
            
            for j in ind:
                temp+=abs(j-i)
            ans.append(temp)
            
        return ans
        
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num=str(num)
        n=int(num)
        count=0
        for i in range(len(num)-k+1):
            if int(num[i:k+i])!=0 and n%int(num[i:k+i])==0:
                count+=1
        return count
            
        
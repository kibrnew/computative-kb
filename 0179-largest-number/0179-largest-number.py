class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        new=list(map(str,nums))
        n=len(nums)
        for i in range(n):
            for j in range(i,n):
                
                if int(new[j]+new[i])>int(new[i]+new[j]):
                    new[i],new[j]=new[j],new[i]
        ans="".join(new)
        if int(ans)==0:
            return "0"
        return ans
        
        
        
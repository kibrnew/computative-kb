class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        new=[]
        ans=[]
        for i in range(len(l)):
            new.append(sorted(nums[l[i]:r[i]+1]))
        for j in new:
            dif=j[1]-j[0]
            b=True
            for k in range(len(j)-1):
                if j[k+1]-j[k] != dif:
                    b=False
            ans.append(b)
        return ans 
                
                
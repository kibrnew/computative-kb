class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        zero=0
        for i in nums:
            if i==0:
                zero+=1
                continue
            else:
                p*=i
        l=[]
        if zero>0:
            l=[0]*len(nums)
            if zero==1:
                l[nums.index(0)]=p 
        else:
            for i in range(len(nums)):
                l.append(p//nums[i])
        return l
        
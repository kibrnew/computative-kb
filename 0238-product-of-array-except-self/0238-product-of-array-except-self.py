class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
      
        p=1
        zero=0
        for val in nums:
            if val==0:
                zero+=1
            else:
                p*=val
                
        ans=[0]*n
       
        if zero==1:
            ans[nums.index(0)]=p
        if zero==0:
            for i in range(n):
                ans[i]=p//nums[i]
        return ans
        
        
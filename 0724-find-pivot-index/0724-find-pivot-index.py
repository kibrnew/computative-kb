class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum1=[0]*(len(nums))
        for i in range(len(nums)):
            sum1[i]=sum1[i-1]+nums[i]
        for i in range(len(nums)):
            if (sum1[-1]-nums[i])/2 == (sum1[i]-nums[i]):
                return i
        return -1
                
        
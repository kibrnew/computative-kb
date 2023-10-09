class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        mini=nums[0]
        for i in nums[1:]:
            mini=mini&i
        
        pr1=nums[0]
        count=0
        # print(mini)
        # print(22&21)
        # print(29&22)
        # print(nums)
        if mini>0:
            return 1
        for i in nums:
            if pr1==-5:
                pr1=i
            if pr1&i==mini:
                pr1=-5
                count+=1
            else:
                pr1=pr1&i
        return count 
            
        
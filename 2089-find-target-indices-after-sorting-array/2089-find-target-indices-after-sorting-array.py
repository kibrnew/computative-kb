class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count=0
        num=0
        for i in range(len(nums)):
            if nums[i]<target:
                count=count+1
            if nums[i]==target:
                num=num+1
        ans= [j for j in range(count,(count+num))]
        return ans 
            
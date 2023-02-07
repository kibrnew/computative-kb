class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(i,len(nums)-1):
                if nums[i]==nums[j+1]:
                    count+=1
        return count
        
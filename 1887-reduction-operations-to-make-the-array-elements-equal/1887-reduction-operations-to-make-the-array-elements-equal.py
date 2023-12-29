class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        count = 0
        nums.sort()
        size = len(nums)
        for i in range(size - 1, 0, -1):
            if nums[i - 1] != nums[i]:
                count += size - i
        return count
            
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=len(nums)
        j=nums.count(val)
        for _ in range(j):
            nums.remove(val)
        return len(nums)
             
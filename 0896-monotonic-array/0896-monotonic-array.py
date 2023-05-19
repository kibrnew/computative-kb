class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        nums2=sorted(nums)
        return nums2==nums or nums2==nums[::-1]
        
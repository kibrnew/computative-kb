class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)
        res = []
        for num in nums1:
            if num in nums2:
                count = min(nums1[num], nums2[num])
                res.extend([num]*count)
        return res
        
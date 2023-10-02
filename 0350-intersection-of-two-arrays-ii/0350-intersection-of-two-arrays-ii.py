class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count=Counter(nums1)
        ans=[]
        for num in nums2:
            if count[num]>0:
                count[num]-=1
                ans.append(num)
        return ans
        
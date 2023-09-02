class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums1)
        m=len(nums2)
        ans=[-1]*n
        for i in range(n):
            stack=nums2[::-1]
            for j in range (m):
                temp=stack.pop()
                if nums1[i]==temp:
                    while stack:
                        temp=stack.pop()
                        if temp>nums1[i]:
                            ans[i]=temp
                            break
                    break
        return ans 
        
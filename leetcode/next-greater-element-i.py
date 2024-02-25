class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def greaterElement(nums1,nums2):
            ans=[]
            d={}
            stack=[]
            for val in nums2:
                while stack and stack[-1]<val:
                    d[stack.pop()]=val
                stack.append(val)

            for val in nums1:
                if val not in d:
                    ans.append(-1)
                else:
                    ans.append(d[val])
            return ans
        return (greaterElement(nums1,nums2))
        
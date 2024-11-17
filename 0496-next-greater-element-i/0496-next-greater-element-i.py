class Solution:
    def nextGreaterElement(self, nums1: List[int], nums: List[int]) -> List[int]:

        n=len(nums)
        ans=[-1]*n
        ind=Counter()
        stack=[]
        for i in range(n):
            while stack and nums[stack[-1]]<nums[i]:
                cur=stack.pop()
                ans[cur]=nums[i]

            ind[nums[i]]=i
            stack.append(i)

        res=[]
        for i in nums1:
            res.append(ans[ind[i]])

        return res 

                
        
        
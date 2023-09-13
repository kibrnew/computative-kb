class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        stack=[]
        ans=[-1]*n
        for i in range(n*2):
            while stack and nums[stack[-1]]<nums[i%n]:
                ans[stack.pop()]=nums[i%n]
            stack.append(i%n)
        return ans
        
        
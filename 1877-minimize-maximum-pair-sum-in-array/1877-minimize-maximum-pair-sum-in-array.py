class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans=[]
        pr2=len(nums)-1
        for i in range(len(nums)//2):
            ans.append(nums[i]+nums[pr2-i])
        return max(ans)
        
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        @cache
        def dfs(i,op):
            if i==len(nums):
                    return 0
            if op=="+":
                return max(dfs(i+1,"-")+nums[i],dfs(i+1,"+"))
            else:
                return max(dfs(i+1,"+")-nums[i],dfs(i+1,"-"))
                
        return dfs(0,"+")
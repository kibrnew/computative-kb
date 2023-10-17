class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        cache = {}
        def dfs(i,op):
            if i==len(nums):
                return 0
            if (i, op) in cache:
                return cache[(i, op)] 
            
            if op=="+":
                cache[(i, op)] = max(dfs(i+1,"-")+nums[i],dfs(i+1,"+"))
                return cache[(i, op)]
            else:
                cache[(i, op)]=max(dfs(i+1,"+")-nums[i],dfs(i+1,"-"))
                return cache[(i, op)]
                
        return dfs(0,"+")
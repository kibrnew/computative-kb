class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target=sum(nums)
        if target%2==1:
            return False
        target//=2
        
        dp={}
        def dfs(i,s):
            
            if i>=len(nums):
                return False
            if s>target:
                return False 
            if (i,s) in dp:
                return dp[(i,s)]
            if s==target:
                return True
            dp[(i,s)]=dfs(i+1,s) or dfs(i+1,s+nums[i])
            return dp[(i,s)]
            
        return dfs(0,0)

                
            
        
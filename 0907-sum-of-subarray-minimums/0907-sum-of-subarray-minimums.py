class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        ans=0
        stack=[-1]
        nums=arr+[-1]
        n=len(nums)
       
        for i in range(n):
            while stack and nums[stack[-1]]>nums[i]:
                ind=stack.pop()
                ans+=(i-ind)*(ind-stack[-1])*nums[ind]
                ans%=(10**9+7)
             
            stack.append(i)
                
        return ans%(10**9+7)
            
                
                
                
                
            
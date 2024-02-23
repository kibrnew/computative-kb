class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        ans=0
        stack=[-1]
  
        nums=arr+[-1]
        n=len(nums)
        right=[0]*(n)
        left=[0]*(n)

        for i in range(n):
            while stack and nums[stack[-1]]>nums[i]:
                ind=stack.pop()
                right[ind]=i-ind
                left[ind]=ind-stack[-1]

            
        
            stack.append(i)

 
        left.pop()
        right.pop()
        # print(right)
        # print(left)

        
        ans=0
        for i,(a,b) in enumerate(zip(left,right)):
            ans+=a*b*arr[i]
            ans%=(10**9+7)
    
                
        return ans%(10**9+7)
            
                
                
                
                
            
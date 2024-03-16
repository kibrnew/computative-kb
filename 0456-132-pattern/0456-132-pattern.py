class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        mini = list(accumulate(nums, min))
        stack=[] 
        n = len(nums)
        print(mini)
        
        for i in range(n-1, -1, -1):
        
            if nums[i] > mini[i]:
                
                while stack and stack[-1] <= mini[i]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True
                
                stack.append(nums[i])        
        
        return False
        
      
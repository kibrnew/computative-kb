class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        stack = []
        mini = float('-inf')
        
        for val in reversed(nums):

            if val < mini:
                return True

            while stack and stack[-1] < val:
                mini = stack.pop()

            stack.append(val)

        return False
        
      
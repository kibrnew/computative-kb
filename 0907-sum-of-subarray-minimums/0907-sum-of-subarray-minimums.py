class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []  # Stack to store the indices of elements in ascending order
        
        # Arrays to store left and right boundaries for each element
        left_boundaries = [0] * len(arr)
        right_boundaries = [0] * len(arr)
        
        # Find the left boundaries for each element
        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            if stack:
                left_boundaries[i] = stack[-1] + 1
            else:
                left_boundaries[i] = 0
            stack.append(i)
        
        stack = []  # Reset the stack
        
        # Find the right boundaries for each element
        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            if stack:
                right_boundaries[i] = stack[-1] - 1
            else:
                right_boundaries[i] = len(arr) - 1
            stack.append(i)
        
        # Calculate the sum of minimums for all subarrays
        result = 0
        for i in range(len(arr)):
            result += arr[i] * (i - left_boundaries[i] + 1) * (right_boundaries[i] - i + 1)
            result %= MOD
        
        return result

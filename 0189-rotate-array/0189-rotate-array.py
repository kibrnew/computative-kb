class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pr1=0
        n=len(nums)
        k=k%n
        for i in range(n//2):
            nums[i],nums[-1-i]=nums[-i-1],nums[i]
        # print(nums)
        for i in range(k//2):
            nums[i],nums[k-i-1]=nums[k-i-1],nums[i]
        # print(nums)
        for i in range(k,(n+k)//2):
            nums[i],nums[n+k-i-1]=nums[n+k-i-1],nums[i]
            
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans=[]
        size=len(nums)
        k=k%size
        for i in range(1,size+1):
            if i<=k:
                ans.append(nums[size-k+i-1])
            else:
                ans.append(nums[i-k-1]) 
                
        nums[0:] = ans
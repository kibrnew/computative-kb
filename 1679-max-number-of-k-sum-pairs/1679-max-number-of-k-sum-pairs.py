class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pr1=0
        pr2=len(nums)-1
        nums.sort()
        count=0
        while pr1<pr2:
            summ=nums[pr1]+nums[pr2]
            if summ == k:
                count+=1
                pr1+=1
                pr2-=1
            elif summ<k:
                pr1+=1
            else:
                pr2-=1
        return count
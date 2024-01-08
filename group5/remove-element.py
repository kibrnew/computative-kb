class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        b=[]
        for i in range(len(nums)):
            if nums[i]==val:
                continue 
            else :
                b.append(nums[i])
        nums[:]=b[:]
        return (len(nums))

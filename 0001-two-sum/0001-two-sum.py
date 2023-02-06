class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp=sorted(nums)
        pointer1=0
        pointer2=len(nums)-1
        for i in range(len(nums)):
            if pointer1<len(nums) and pointer2<len(nums):
                summ=temp[pointer1]+temp[pointer2]
                if summ==target:
                    if temp[pointer1] == temp[pointer2]:
                        loc=nums.index(temp[pointer1])
                        nums.pop(loc)
                        return[loc,(nums.index(temp[pointer1])+1)]
                    return  [nums.index(temp[pointer1]),nums.index(temp[pointer2])]
                elif summ<target:
                    pointer1=pointer1+1
                elif summ>target:
                    pointer2=pointer2-1
    
        
        
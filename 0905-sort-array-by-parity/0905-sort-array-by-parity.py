class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr=[]
        arr2=[]
        for i in nums:
            if i%2==0:
                arr.append(i)
            else :
                arr2.append(i)
        return arr+arr2
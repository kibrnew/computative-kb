class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans=[]
        temp=[]
        def backtrack(i):
            ans.append(list(temp))
            if i==len(nums):
                return
        
            for j in range(i,len(nums)):
                temp.append(nums[j])
                backtrack(j+1)
                temp.pop()

        backtrack(0)

        return ans



            
        
        
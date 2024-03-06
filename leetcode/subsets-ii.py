class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans=[]
        temp=[]
        def backtrack(i):
            ans.append(list(temp))

            poped=-20
            for j in range(i,len(nums)):
                if nums[j]!=poped:
                    temp.append(nums[j])
                    backtrack(j+1)
                    poped=temp.pop()

        backtrack(0)
        return ans 
       
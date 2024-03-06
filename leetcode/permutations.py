class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        temp=[]
        ans=[]
        def backtrack():
            if len(temp)==len(nums):
                ans.append(list(temp))
                return 
            for val in nums:
                if val not in temp:
                    temp.append(val)
                    backtrack()
                    temp.pop()

        backtrack()
        return ans 

            

            
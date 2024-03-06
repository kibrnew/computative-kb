class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        nums=sorted(candidates)
        ans=[]
        temp=[]

        # print(nums)

        def backtrack(i,s):
            # print(temp,i,s)
            if target==s:
                ans.append(list(temp))
                return 
            if target<s:
                return 

            poped=-100
            for j in range(i,len(nums)):
                if nums[j]!=poped:
                    s+=nums[j]
                    temp.append(nums[j])
                    backtrack(j+1,s)
                    poped=temp.pop()
                    s-=nums[j]


        backtrack(0,0)

        return ans 

        